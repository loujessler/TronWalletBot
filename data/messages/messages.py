from utils.wallet_func.price_info import get_ticker

import aiogram.utils.markdown as fmt


class Messages:
    def __init__(self, user):
        self.user = user

    menu = {
        'ru': fmt.text(f'Используйте бота @tron как криптовалютный кошелек по умолчанию. '
                       f'Кошелек привязан к вашему аккаунту Telegram.\n\n',
                       f'Отправляйте, получайте и обменивайте криптовалюту.\n\n',
                       f'Присоединяйтесь к нашему каналу, чтобы быть в курсе последних новостей мира '
                       f'криптовалют и Tron, а также новостей сервиса @tron.'),
        'en': fmt.text(f'Use the @tron bot as your regular cryptocurrency wallet. '
                       f'The wallet is linked to your Telegram account.\n\n',
                       f'Send, receive, and exchange cryptocurrencies.\n\n',
                       f'Join our channel to be up to date with the latest crypto world, '
                       f'Tron, and @tron news.'),
    }

    @staticmethod
    def my_wallet(user, balance):
        convert = round(float(balance) * float(get_ticker(coin1='tron', coin2=user.currency)), 2)
        message = {
            'ru': fmt.text(fmt.hbold('💰 Мой кошелек\n'),
                           '\n',
                           'Bitcoin: 0 BTC\n',
                           '\n',
                           'Tron: ', balance, 'TRX  ≈ ',
                           convert,
                           user.currency.upper()),
            'en': fmt.text(fmt.hbold('💰 My wallet\n'),
                           '\n',
                           'Bitcoin: 0 BTC\n',
                           '\n',
                           'Tron: ', balance, 'TRX  ≈ ',
                           convert,
                           user.currency.upper()),
        }
        return message

    def deposit_wallet(self):
        message = {
            'ru': fmt.text(fmt.hbold('➕ Пополнение: TRX\n'),
                           '\n',
                           'Используйте адрес ниже для пополнения  TRX на кошелек бота.\n',
                           '\n'
                           'Сеть: TRON Network - TRON (TRC 20).\n',
                           '\n',
                           fmt.hcode(self), '\n',
                           '\n',
                           'Средства будут зачислены в течение 2 минут.'),
            'en': fmt.text(fmt.hbold('➕ Deposit: TRX\n'),
                           '\n',
                           'Use the address below to deposit TRX to the bot wallet.\n',
                           '\n'
                           'Network: TRON Network - TRON (TRC 20).\n',
                           '\n',
                           fmt.hcode(self), '\n',
                           '\n',
                           'Funds will be credited within 2 minutes'),
        }
        return message
