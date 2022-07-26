# import asyncio
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
# import bcrypt
# from aiogram.types import CallbackQuery
#
# from keyboards.default import kb_menu, kb_okey
# from loader import dp
#
# from states import Regist_pas
#
# #
# # @dp.message_handler(Command('password'))
# # async def reg_pas(message: types.Message):
# #     await message.delete()
# #     msg = await message.answer('Введите пароль:', reply_markup=None)
# #     await Regist_pas.password.set()
# #     await asyncio.sleep(5)
# #     await dp.bot.delete_message(message.chat.id, msg.message_id)
#
#
# @dp.message_handler(state=Regist_pas.password)
# async def state_password(message: types.Message, state: FSMContext):
#     hashed = bcrypt.hashpw(bytes(message.text, 'utf-8'), bcrypt.gensalt(7))
#
#     await state.update_data(password=message.text)
#     await message.delete()
#     if bcrypt.checkpw(bytes(message.text, 'utf-8'), hashed):
#         stiker = await message.answer_sticker(sticker='CAACAgIAAxkBAAEE5FZil_BG4nu2OBOQjliEA2MKnooOegACxAADMNSdEcjFvLwK6xVKJAQ')
#         msg = await message.answer(f'Ваш пароль: {message.text}\n'
#                                    f'Это сообщение самоуничтожится', protect_content=True, reply_markup=kb_okey)
#     await state.finish()
#     await asyncio.sleep(2)
#     await dp.bot.delete_message(message.chat.id, msg.message_id)
#     await dp.bot.delete_message(message.chat.id, stiker.message_id)
#
#
# # @dp.message_handler(text='/password')
# # async def write_password(message: types.Message):
# #     await message.reply("Напиши пароль!")
# #     await Dialog.password.set()
# #
# #
# # @dp.message_handler(state=Dialog.password)
# # async def set_password(message: types.Message, state: FSMContext):
# #     # password = bytes(message.text, 'utf-8')
# #     hashed = bcrypt.hashpw(bytes(message.text, 'utf-8'), bcrypt.gensalt(7))
# #     # hashed2 = bcrypt.hashpw(bytes(message.text+"hhff", 'utf-8'), bcrypt.gensalt(7))
# #     if bcrypt.checkpw(bytes(message.text, 'utf-8'), hashed):
# #         await message.reply(f"Твой пароль: {message.text}")
# #     else:
# #         await message.reply("Не верный пароль! Введи ещё раз!")
# #     await state.finish()
