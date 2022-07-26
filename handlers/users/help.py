from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('help'))
async def command_help(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}!\n'
                         f'Тебе нужна помощь?')
