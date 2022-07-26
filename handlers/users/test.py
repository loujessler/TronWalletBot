from aiogram import types

from keyboards.default import kb_test
from loader import dp


@dp.message_handler(text='Любой текст')
async def command_test(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}!\n'
                         f'Change keyboard?', reply_markup=kb_test)
