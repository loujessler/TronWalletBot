from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'yes': {
        'ru': 'Да',
        'en': 'Yes'
    },
    'no': {
        'ru': 'Нет',
        'en': 'No'
    },
}


def ikb_menu_yes_no(user, call_salt=''):
    ikb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['yes'][user.language],
                                                            callback_data='yes'+call_salt),
                                       InlineKeyboardButton(text=texts['no'][user.language],
                                                            callback_data='no'+call_salt)
                                   ],
                               ])
    return ikb
