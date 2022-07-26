from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.languages import languages


ikb_languages = InlineKeyboardMarkup(row_width=3)
for language in languages:
    ikb_languages.insert(InlineKeyboardButton(text=languages.get(language), callback_data=language))

