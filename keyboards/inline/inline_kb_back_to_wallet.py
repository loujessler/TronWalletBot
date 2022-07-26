from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'back': {
        'ru': '🔙 Назад в кошелек',
        'en': '🔙 Back to wallet'
    },
}


def ikb_menu_back_to_wallet(user):
    ikb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back to wallet'),
                                   ],
                               ])
    return ikb
