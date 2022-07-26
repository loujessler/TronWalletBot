from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'standard': {
        'ru': '🔑 Изменить пароль',
        'en': '🔑 Change password'
    },
    'priv': {
        'ru': '🔐 Изменить пароль с приватным ключом',
        'en': '🔐 Change password with private key'
    },
    'back': {
        'ru': '🔙 Назад',
        'en': '🔙 Back'
    },
}


def ikb_change_password_menu(user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['standard'][user.language],
                                                            callback_data='change_password_standard')
                                   ], [
                                       InlineKeyboardButton(
                                           text=texts['priv'][user.language],
                                           callback_data='change_password_with_priv')
                                   ], [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back')
                                   ],
                               ]
                               )
    return ikb
