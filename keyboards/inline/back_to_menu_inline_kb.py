from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'back': {
        'ru': '🔙 Назад',
        'en': '🔙 Back'
    },
}


def ikb_menu_back_to_menu(user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back'),
                                   ],
                               ])
    return ikb
