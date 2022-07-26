from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'deposit': {
        'ru': '➕ Пополнить',
        'en': '➕ Deposit'
    },
    'back': {
        'ru': '🔙 Назад',
        'en': '🔙 Back'
    },
}


def ikb_menu_zero_balance(user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['deposit'][user.language],
                                                            callback_data='deposit'),
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back')
                                   ],
                               ])
    return ikb
