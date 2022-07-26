from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_okey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='okey 👍', callback_data='okey'),
        ],
    ],
    resize_keyboard=True
)
