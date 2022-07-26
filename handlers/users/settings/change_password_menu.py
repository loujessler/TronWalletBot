
from keyboards.inline.settings import ikb_change_password_menu
from loader import dp
from aiogram import types
from aiogram.types import ParseMode

from data.messages.settings_messages import Messages
from utils.db_api import quick_commands as commands


@dp.callback_query_handler(text='change password')
async def change_password_menu_command(call: types.CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await call.message.edit_text(Messages.change_password_menu[user.language], parse_mode='HTML')
    await call.message.edit_reply_markup(reply_markup=ikb_change_password_menu(user))
