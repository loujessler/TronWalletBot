from aiogram.dispatcher import FSMContext

from data.languages import languages
from keyboards.inline.language_inline_kb import ikb_languages
from keyboards.inline.settings import ikb_back_to_settings
from loader import dp, bot
from aiogram import types

from data.messages.settings_messages import Messages
from states.regist import Regist
from utils.db_api import quick_commands as commands
from utils.edit_last_message import EditLastMessage
from utils.set_bot_commands import set_start_commands

edit_ls = EditLastMessage(bot)


@dp.callback_query_handler(text='change_language')
async def write_last_password(call: types.CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(
        Messages.change_language[user.language],
        call,
        ikb_languages
    )
    await Regist.language.set()


@dp.callback_query_handler(lambda c: c.data in [language for language in languages], state=Regist.language)
async def create_password(call: types.CallbackQuery, state: FSMContext):
    user = await commands.select_user(call.from_user.id)
    await commands.update_language(user.user_id, call.data)
    user = await commands.select_user(call.from_user.id)
    await set_start_commands(call.bot, call.from_user.id, user.language)
    await edit_ls.edit_last_message(
        Messages.change_language_done[user.language],
        call,
        ikb_back_to_settings(user)
    )
    await state.finish()
