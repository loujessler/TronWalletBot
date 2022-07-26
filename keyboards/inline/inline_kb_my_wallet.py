from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'deposit': {
        'ru': '⤵️ Пополнить',
        'en': '⤵️ Deposit'
    },
    'withdraw': {
        'ru': 'Вывести ⤴️',
        'en': 'Withdraw ⤴️'
    },
    'bandwidth': {
        'ru': '🚀️ Пропускная способность',
        'en': '🚀️ Bandwidth'
    },
    'back': {
        'ru': '🔙 Назад',
        'en': '🔙 Back'
    },
}


def ikb_menu_my_wallet(user):
    ikb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['deposit'][user.language],
                                                            callback_data='deposit'),
                                       InlineKeyboardButton(text=texts['withdraw'][user.language],
                                                            callback_data='withdraw'),
                                   ], [
                                       InlineKeyboardButton(text=texts['bandwidth'][user.language],
                                                            callback_data='bandwidth')
                                   ], [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back')
                                   ],
                               ])
    return ikb
