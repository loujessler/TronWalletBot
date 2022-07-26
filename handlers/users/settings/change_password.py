from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters import IsCorrectPassword, IsPrivate, IsCorrectPrivateKey
from keyboards.inline import ikb_menu_back_to_menu
from keyboards.inline.settings import ikb_back_to_settings, ikb_menu_settings
from loader import dp, bot
from aiogram import types
from aiogram.types import ParseMode

from data.messages.settings_messages import Messages
from states.change_password_state import Change_password
from utils.db_api import quick_commands as commands
from utils.edit_last_message import EditLastMessage
from utils.encryption import decrypt_xor, encrypt_xor

edit_ls = EditLastMessage(bot)


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)
    data = await state.get_state()
    await message.delete()
    if data is None:
        return
    await state.finish()
    # await message.answer(Messages.menu, reply_markup=ikb_menu_settings, parse_mode=ParseMode.MARKDOWN)
    await edit_ls.edit_last_message(Messages(user).menu_msg()[user.language], message, ikb_menu_settings(user))
    # await bot.edit_message_reply_markup(reply_markup=ikb_menu_settings)


@dp.callback_query_handler(text='change_password_standard')
async def write_last_password(call: types.CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await call.message.edit_text(Messages.change_password[0][user.language], parse_mode='HTML')
    await Change_password.last_password.set()


###Проверяем пароль
@dp.message_handler(IsCorrectPassword(), state=Change_password.last_password)
async def process_password_invalid(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await bot.delete_message(message.from_user.id, message.message_id)
    await edit_ls.edit_last_message(Messages.password_incorrect(message.text)[user.language], message)


###Изменение пароля при помощи приватного ключа
@dp.callback_query_handler(text='change_password_with_priv')
async def write_private_key(call: types.CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await call.message.edit_text(Messages.change_password[5][user.language], parse_mode='HTML')
    await Change_password.private_key.set()


###Проверяем приватный ключ
@dp.message_handler(IsCorrectPrivateKey(), state=Change_password.private_key)
async def process_private_key_invalid(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await bot.delete_message(message.from_user.id, message.message_id)
    await edit_ls.edit_last_message(Messages.private_key_incorrect[user.language], message)


async def delete_last_message_st_pr_ls(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await bot.delete_message(message.from_user.id, message.message_id)
    await edit_ls.edit_last_message(Messages.change_password[1][user.language], message)


@dp.message_handler(IsPrivate(), state=Change_password.last_password)
async def update_password_state(message: types.Message, state: FSMContext):
    await state.update_data(last_password=message.text)
    await delete_last_message_st_pr_ls(message)
    await Change_password.password.set()


@dp.message_handler(IsPrivate(), state=Change_password.private_key)
async def update_password_state(message: types.Message, state: FSMContext):
    await state.update_data(private_key=message.text)
    await delete_last_message_st_pr_ls(message)
    await Change_password.password.set()


@dp.message_handler(IsPrivate(), state=Change_password.password)
async def write_reply_new_password(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)
    await state.update_data(password=message.text)
    await bot.delete_message(message.from_user.id, message.message_id)
    await edit_ls.edit_last_message(Messages.change_password[2][user.language], message)
    await Change_password.reply_password.set()


@dp.message_handler(IsPrivate(), state=Change_password.reply_password)
async def update_password_standard(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)
    await state.update_data(reply_password=message.text)
    data = await state.get_data()
    await bot.delete_message(message.from_user.id, message.message_id)
    if data.get('password') != data.get('reply_password'):
        await edit_ls.edit_last_message(Messages.change_password[3][user.language], message)
    else:
        data = await state.get_data()
        if data.get('last_password') is not None:
            _priv = decrypt_xor(
                user.private_key[3:len(user.private_key) - 3],
                data.get('last_password'))
            await commands.update_private_key(user.user_id, _priv[3:6] +
                                              encrypt_xor(_priv, data.get('password')) +
                                              _priv[len(_priv) - 6:len(_priv) - 3]
                                              )

        elif data.get('private_key') is not None:
            await commands.update_private_key(user.user_id, data.get('private_key')[3:6] +
                                              encrypt_xor(data.get('private_key'), data.get('password')) +
                                              data.get('private_key')[
                                              len(data.get('private_key')) - 6:len(data.get('private_key')) - 3]
                                              )
        await edit_ls.edit_last_message(Messages.change_password[4][user.language], message, ikb_back_to_settings(user))
        await state.finish()
        # i = 0
        # while True:
        #     try:
        #         await bot.edit_message_text(Messages.change_password[4],
        #                                     message.from_user.id,
        #                                     (message.message_id - i),
        #                                     reply_markup=ikb_menu_back_to_menu,
        #                                     parse_mode=ParseMode.MARKDOWN)
        #         await state.finish()
        #         break
        #     except Exception:
        #         i += 1
        #         pass
