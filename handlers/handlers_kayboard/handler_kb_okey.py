from aiogram import types

from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(text='okey 👍')
async def finish_func(message: types.Message):
    # await message.edit_reply_markup(reply_markup=kb_menu)
    await message.delete()
    await message.answer('Выберете следующее меню', reply_markup=kb_menu)

