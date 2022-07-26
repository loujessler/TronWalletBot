from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'wallet': {
        'ru': '💰 Мой кошелек',
        'en': '💰 My wallet'
    },
    'checks': {
        'ru': '🧾 Чеки',
        'en': '🧾 Checks'
    },
    'support': {
        'ru': '💬 Поддержка',
        'en': '💬 Support'
    },
    'settings': {
        'ru': '⚙️ Настройки',
        'en': '⚙️ Settings'
    },
}


def ikb_menu(user):
    ikb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['wallet'][user.language],
                                                            callback_data='my wallet'),
                                       InlineKeyboardButton(text=texts['checks'][user.language],
                                                            callback_data='checks'),
                                   ],
                                   [
                                       InlineKeyboardButton(text=texts['support'][user.language],
                                                            callback_data='support'),
                                       InlineKeyboardButton(text=texts['settings'][user.language],
                                                            callback_data='my settings'),
                                   ],
                               ])
    return ikb
