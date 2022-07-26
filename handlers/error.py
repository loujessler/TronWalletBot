from aiogram import types
from loader import dp

from utils.db_api import quick_commands as commands


@dp.message_handler()
async def command_error(message: types.Message):
    # try:
    #     await commands.select_user(message.from_user.id)
    #     await message.answer(f'Вы ещё не зарегистрированы. \nДля регистрации нажмите /start')
    # except Exception:

    await message.answer(f'Такой команды: "{message.text}" нет.')
