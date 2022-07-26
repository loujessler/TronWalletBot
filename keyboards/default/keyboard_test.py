from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/menu'),
        ],
    ],
    resize_keyboard=True
)
