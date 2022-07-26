from aiogram import types
from aiogram.dispatcher.filters import Command

from data.messages.messages import Messages
from filters import HaveInDb, IsPrivate
from keyboards.inline import ikb_menu
from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(Command('menu'), HaveInDb(True))
async def menu(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.delete()
    await message.answer(Messages.menu[user.language], reply_markup=ikb_menu(user))
