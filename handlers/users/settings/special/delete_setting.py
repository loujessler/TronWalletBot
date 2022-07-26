from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from handlers.users.bot_start import edit_ls
from loader import dp
from filters import IsCorrectPassword

from handlers.users.settings.settings_menu import special_settings_menu_command
from keyboards.inline import ikb_menu_yes_no
from keyboards.inline.settings.inline_kb_settings import ikb_special_settings

from data.messages.settings_messages import Messages
from states.delete_wallet import DeleteWallet
from utils.db_api import quick_commands as commands

# Добавляем возможность отмены, если пользователь передумал заполнять
from utils.encryption import encrypt_xor
from utils.wallet_func.wallet_func import create_wallet


@dp.message_handler(state='*', commands='cancel_delete')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: Message, state: FSMContext):
    await message.delete()
    state_cancel = await state.get_state()
    if state_cancel is None:
        return
    await state.finish()
    await special_settings_menu_command(message)


@dp.callback_query_handler(text='delete')
async def delete_question(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Messages(user).delete_msg[user.language],
                                    call,
                                    ikb_menu_yes_no(user, '_delete'))


@dp.callback_query_handler(text='no_delete')
async def special_rec_no_command(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Messages(user).special_settings[user.language],
                                    call,
                                    ikb_special_settings(user))


@dp.callback_query_handler(text='yes_delete')
async def special_del_password_command(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Messages.password[user.language],
                                    call)
    await DeleteWallet.password.set()


# Проверяем пароль
@dp.message_handler(IsCorrectPassword(), state=DeleteWallet.password)
async def process_del_password_invalid(message: Message):
    user = await commands.select_user(message.from_user.id)
    return await message.answer(Messages.password_invalid('/cancel_delete')[user.language])


@dp.message_handler(state=DeleteWallet.password)
async def special_del_yes_command(message: Message, state: FSMContext):
    password = message.text
    await state.update_data(password=password)
    await message.delete()
    user = await commands.select_user(message.from_user.id)
    wallet = create_wallet()
    await commands.delete_wallet(user.user_id,
                                 wallet=wallet[0],
                                 private_key=(wallet[1][3:6] + encrypt_xor(wallet[1], password) + wallet[1][len(
                                     wallet[1]) - 6:len(wallet[1]) - 3])
                                 )
    user = await commands.select_user(message.from_user.id)
    await edit_ls.edit_last_message(Messages(user).new_wallet_after_del(wallet[1]),
                                    message)
    await state.finish()
