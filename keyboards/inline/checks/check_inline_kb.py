from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.messages.checks_messages import ChecksMessages

texts = {
    'resend': {
        'ru': 'Переслать ↗️',
        'en': 'Resend ↗️'
    },
    'back': {
        'ru': '🔙 Назад',
        'en': '🔙 Back'
    },
}


def ikb_check(user, msg):
    ikb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(
                                           text=texts['resend'][user.language],
                                           switch_inline_query=msg.replace('\.','.') + ChecksMessages(user).check_msg_resend()
                                       ),
                                   ], [
                                       InlineKeyboardButton(
                                           text=texts['back'][user.language],
                                           callback_data='back')
                                   ],
                               ])
    return ikb
