from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

texts = {
    'draw_check': {
        'ru': 'Выписать чек',
        'en': 'Draw a check'
    },
    'back': {
        'ru': '🔙 Назад',
        'en': '🔙 Back'
    },
}


def ikb_menu_checks(user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['draw_check'][user.language],
                                                            callback_data='draw_check')
                                   ], [
                                       InlineKeyboardButton(text=' ',
                                                            callback_data=' ')
                                   ], [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back')
                                   ],
                               ]
                               )
    return ikb
