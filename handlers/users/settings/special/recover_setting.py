from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters import IsCorrectPassword
from handlers.users.bot_start import edit_ls
from handlers.users.settings.settings_menu import special_settings_menu_command
from keyboards.inline import ikb_menu_yes_no
from keyboards.inline.settings import ikb_menu_settings
from keyboards.inline.settings.inline_kb_settings import ikb_special_settings
from loader import dp
from aiogram.types import CallbackQuery, Message

from data.messages.settings_messages import Messages
from states.recovery_wallet import RecoveryWallet
from utils.db_api import quick_commands as commands
from utils.encryption import encrypt_xor
from utils.wallet_func.wallet_func import take_address


@dp.message_handler(state='*', commands='cancel_recovery')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: Message, state: FSMContext):
    await message.delete()
    state_cancel = await state.get_state()
    if state_cancel is None:
        return
    await state.finish()
    await special_settings_menu_command(message)


@dp.callback_query_handler(text='recover')
async def recover_question(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Messages(user).recovery_msg[user.language],
                                    call,
                                    ikb_menu_yes_no(user, '_recover'))


@dp.callback_query_handler(text='no_recover')
async def special_rec_no_command(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Messages(user).special_settings[user.language],
                                    call,
                                    ikb_special_settings(user))


@dp.callback_query_handler(text='yes_recover')
async def special_rec_password_command(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Messages.password[user.language],
                                    call)
    await RecoveryWallet.password.set()


# Проверяем пароль
@dp.message_handler(IsCorrectPassword(), state=RecoveryWallet.password)
async def process_rec_password_invalid(message: Message):
    user = await commands.select_user(message.from_user.id)
    return await message.answer(Messages.password_invalid('/cancel_recovery')[user.language])


@dp.message_handler(state=RecoveryWallet.password)
async def special_rec_private_command(message: Message, state: FSMContext):
    await message.delete()
    await state.update_data(password=message.text)
    user = await commands.select_user(message.from_user.id)
    await edit_ls.edit_last_message(Messages.private_key[user.language], message)
    await RecoveryWallet.private_key.set()


@dp.message_handler(state=RecoveryWallet.private_key)
async def special_rec_yes_command(message: Message, state: FSMContext):
    await message.delete()
    user = await commands.select_user(message.from_user.id)
    await state.update_data(private_key=message.text)
    data = await state.get_data()
    wallet = [
        take_address(data.get('private_key')),
        data.get('private_key')
    ]
    if wallet[0] is not False:
        await commands.delete_wallet(user.user_id,
                                     wallet=wallet[0],
                                     private_key=(wallet[1][3:6] + encrypt_xor(wallet[1], data.get('password'))
                                                  + wallet[1][len(wallet[1]) - 6:len(wallet[1]) - 3])
                                     )
        user = await commands.select_user(message.from_user.id)
        await edit_ls.edit_last_message(Messages(user).new_wallet_after_rec(),
                                        message)
        await state.finish()
    else:
        await edit_ls.edit_last_message(Messages(user).private_key_invalid('/cancel_recovery'),
                                        message)
        await state.set_state(RecoveryWallet.private_key)



    # await state.update_data(password=password)
    # await message.delete()
    # user = await commands.select_user(message.from_user.id)
    # wallet = create_wallet()
    # await commands.delete_wallet(user.user_id,
    #                              wallet=wallet[0],
    #                              private_key=(wallet[1][3:6] + encrypt_xor(wallet[1], password) + wallet[1][len(
    #                                  wallet[1]) - 6:len(wallet[1]) - 3])
    #                              )
    # user = await commands.select_user(message.from_user.id)
    # await edit_ls.edit_last_message(Messages(user).new_wallet_after_del(wallet[1]),
    #                                 message)
    # await state.finish()
