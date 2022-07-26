from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='11'),
        ],
        [
            KeyboardButton(text='100'),
        ],
        [
            KeyboardButton(text='Любой текст'),
            KeyboardButton(text='Инлайн меню'),
            KeyboardButton(text='лайк'),
        ],
    ],
    resize_keyboard=True
)
