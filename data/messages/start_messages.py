import aiogram.utils.markdown as fmt
from utils.db_api import quick_commands as commands


class Messages:
    def __init__(self, user):
        self.user = user

    @staticmethod
    def language_mes(aio_type):
        text = fmt.text(
            f'✌️ Hi, {aio_type.from_user.first_name}.\n',
            fmt.hbold('🏳️ Choose your language: ')
        )
        return text

    @staticmethod
    def you_have_wallet(user):
        text = {
            'ru': fmt.text(
                f'✌️ Привет, {user.first_name}.\n\n',
                f'💰 У вас уже есть кошелёк:\n\n',
                fmt.hcode(user.wallet)
            ),
            'en': fmt.text(
                f'✌️ Hi, {user.first_name}.\n\n',
                f'💰 You already have a wallet:\n\n',
                fmt.hcode(user.wallet)
            ),

        }
        return text[user.language]

    @staticmethod
    def first_pas_mes(language, aio_type):
        text = {
            'ru': fmt.text(
                f'✌️ Привет, {aio_type.from_user.first_name}.\n',
                'Для сохранности ваших данных необходимо защитить паролем.\n\n',
                fmt.hbold('🔑 Введите пароль: ')
            ),
            'en': fmt.text(
                f'✌️ Hi, {aio_type.from_user.first_name}.\n',
                'For the security of your wallet, you must protect it with a password.\n\n',
                fmt.hbold('🔑 Enter password: ')
            ),
        }
        return text[language]

    reply_password = {
        'ru': fmt.text(
            fmt.hbold('🔄 🔑 Повторно введите пароль: ')
        ),
        'en': fmt.text(
            fmt.hbold('🔄 🔑 Reenter password: ')
        ),
    }

    pas_not_match = {
        'ru': fmt.text(
            'Пароли не совпадают\n\n',
            fmt.hbold('🔑 Введите пароль: ')
        ),
        'en': fmt.text(
            "Passwords didn't match\n\n",
            fmt.hbold('🔑 Enter password: ')
        ),
    }

    @staticmethod
    def new_wallet(user, private_key):
        message = {
            'ru': fmt.text(
                fmt.hbold('✨ Вам выдан кошелёк Tron\n\n'),
                '💰 Ваш кошелёк: \n\n',
                fmt.hcode(user.wallet),
                '\n\n',
                '🔐 Ваш приватный ключ: \n\n',
                fmt.hspoiler(private_key),
                '\n\n📝 Обязательно сохраните свой приватный ключ для восстановления кошелька!\n\n',
                'Начни с главного меню ➡️ /menu'
            ),
            'en': fmt.text(
                fmt.hbold('✨ You have been given a Tron wallet\n\n'),
                '💰 Your wallet: \n\n',
                fmt.hcode(user.wallet),
                '\n\n',
                '🔐 Your private key: \n',
                fmt.hspoiler(private_key),
                '\n\n📝 Be sure to save your private key to restore your wallet!\n\n',
                'Start from the main menu ➡️ /menu'
            ),
        }
        return message[user.language]
