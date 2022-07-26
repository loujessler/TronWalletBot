from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.currencies import currencies


def ikb_currencies_func(user_language):
    ikb_currencies = InlineKeyboardMarkup(row_width=3)
    for currency in currencies[user_language]:
        ikb_currencies.insert(
            InlineKeyboardButton(text=currencies[user_language].get(currency), callback_data=currency))
    return ikb_currencies
