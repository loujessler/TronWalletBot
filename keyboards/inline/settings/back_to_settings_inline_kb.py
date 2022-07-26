from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'back': {
        'ru': '🔙 Назад в настройки',
        'en': '🔙 Back to settings'
    },
    'back_menu': {
        'ru': '🔝 В главное меню',
        'en': '🔝 Main menu'
    },
}


def ikb_back_to_settings(user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back_to_settings'),
                                   ], [
                                       InlineKeyboardButton(text=texts['back_menu'][user.language],
                                                            callback_data='back'),
                                   ],
                               ])

    return ikb
