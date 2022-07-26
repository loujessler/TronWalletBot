from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

texts = {
    'transaction': {
        'ru': 'Ссылка на транзакцию',
        'en': 'Transaction link'
    },
    'back': {
        'ru': '🔙 Назад в кошелек',
        'en': '🔙 Back to wallet'
    },
}


async def ikb_link_transaction(txID, user):
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text=texts['transaction'][user.language],
                                                            web_app=WebAppInfo(
                                                                url=f'https://nile.tronscan.org/#/transaction/{txID}'))
                                       # https://tronscan.org/#/transaction/  Mainnet
                                   ], [
                                       InlineKeyboardButton(text=texts['back'][user.language],
                                                            callback_data='back to wallet')
                                   ]
                               ])
    return ikb
