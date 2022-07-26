from aiogram.dispatcher.filters import Command

from filters import HaveInDb
from handlers.users.bot_start import edit_ls
from keyboards.inline.settings import ikb_menu_settings
from keyboards.inline.settings.inline_kb_settings import ikb_special_settings
from loader import dp
from aiogram.types import ParseMode, CallbackQuery, Message

from data.messages.settings_messages import Messages
from utils.db_api import quick_commands as commands


@dp.callback_query_handler(text='back_to_settings')
@dp.callback_query_handler(text='my settings')
async def settings_menu_command(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await call.message.edit_text(Messages(user).menu_msg()[user.language], parse_mode='HTML')
    await call.message.edit_reply_markup(reply_markup=ikb_menu_settings(user))


@dp.message_handler(HaveInDb(True), Command('settings'))
async def settings_menu_command(message: Message):
    user = await commands.select_user(message.from_user.id)
    await message.delete()
    await message.answer(Messages(user).menu_msg()[user.language],
                         reply_markup=ikb_menu_settings(user),
                         parse_mode='HTML')


@dp.callback_query_handler(text='special_settings')
async def special_settings_menu_command(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Messages(user).special_settings[user.language],
                                    call,
                                    ikb_special_settings(user))
    # await call.message.edit_text(Messages(user).special_settings[user.language], parse_mode='HTML')
    # await call.message.edit_reply_markup(reply_markup=ikb_special_settings(user))
