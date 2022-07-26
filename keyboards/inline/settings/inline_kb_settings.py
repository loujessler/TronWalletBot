from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'language': {
        'ru': 'Изменить язык',
        'en': 'Change language'
    },
    'currency': {
        'ru': 'Изменить локальную валюту',
        'en': 'Change local currency'
    },
    'password': {
        'ru': 'Изменить пароль',
        'en': 'Change password'
    },
    'special': {
        'ru': 'Особые настройки',
        'en': 'Special settings'
    },
    'back': {
        'ru': '🔙 Назад',
        'en': '🔙 Back'
    },
    #####Special settings
    'delete': {
        'ru': '❌ УДАЛИТЬ кошелёк ❌',
        'en': '❌ DELETE wallet ❌'
    },
    'recover': {
        'ru': '♻️ Восстановить кошелёк ♻️',
        'en': '♻️ Recover wallet ♻️'
    },
}


def ikb_menu_settings(user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['language'][user.language],
                                                            callback_data='change_language')
                                   ], [
                                       InlineKeyboardButton(text=texts['currency'][user.language],
                                                            callback_data='change_currency')
                                   ], [
                                       InlineKeyboardButton(text=texts['password'][user.language],
                                                            callback_data='change password')
                                   ], [
                                       InlineKeyboardButton(text=texts['special'][user.language],
                                                            callback_data='special_settings')
                                   ], [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back')
                                   ],
                               ]
                               )
    return ikb


def ikb_special_settings(user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['recover'][user.language],
                                                            callback_data='recover')
                                   ], [
                                       InlineKeyboardButton(text=texts['delete'][user.language],
                                                            callback_data='delete')
                                   ], [
                                       InlineKeyboardButton(text=' ', callback_data='nothing')
                                   ], [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back_to_settings')
                                   ],
                               ]
                               )
    return ikb
