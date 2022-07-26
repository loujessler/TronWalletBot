import aiogram.utils.markdown as fmt

from data.currencies import currencies
from data.languages import languages


class Messages:
    def __init__(self, user):
        self.user = user

    def menu_msg(self):
        menu = {
            'ru': fmt.text(
                fmt.hbold('⚙️ Настройки\n\n'),
                f'Язык: {languages[self.user.language]}\n',
                f'Локальная валюта: {currencies[self.user.language][self.user.currency]}'
            ),
            'en': fmt.text(
                fmt.hbold('⚙️ Settings\n\n'),
                f'Language: {languages[self.user.language]}\n',
                f'Local currency: {currencies[self.user.language][self.user.currency]}'
            )
        }
        return menu

    change_password_menu = {
        'ru': fmt.text(
            fmt.hbold('🔑 Изменение пароля')
        ),
        'en': fmt.text(
            fmt.hbold('🔑 Change password')
        ),
    }
    change_password = [
        {
            'ru': fmt.text(
                fmt.hbold('🗝 Введите старый пароль:')  # 0
            ),
            'en': fmt.text(
                fmt.hbold('🗝 Enter old password:')  # 0
            ),
        },
        {
            'ru': fmt.text(
                fmt.hbold('🔑 Введите новый пароль:')  # 1
            ),
            'en': fmt.text(
                fmt.hbold('🔑 Enter a new password:')
            ),
        },
        {
            'ru': fmt.text(
                fmt.hbold('🔄 🔑 Повторите новый пароль:')  # 2
            ),
            'en': fmt.text(
                fmt.hbold('🔄 🔑 Repeat new password:')
            ),
        },
        {
            'ru': fmt.text(
                'Пароли не совпадают\n\n',
                fmt.hbold('🔑 Введите пароль заново: ')  # 3
            ),
            'en': fmt.text(
                'Passwords do not match\n\n',
                fmt.hbold('🔑 Re-enter your password: ')
            ),
        },
        {
            'ru': fmt.text(
                fmt.hbold('🎉 Пароль успешно изменен')  # 4
            ),
            'en': fmt.text(
                fmt.hbold('🎉 Password changed successfully')
            ),
        },
        {
            'ru': fmt.text(
                fmt.hbold('🔐 Введите приватный ключ:')  # 5
            ),
            'en': fmt.text(
                fmt.hbold('🔐 Enter private key:')
            ),
        },
    ]

    @staticmethod
    def password_incorrect(msg):
        text = {
            'ru': fmt.text(
                'Не верный пароль "',
                fmt.hbold(msg),
                '". \nПовторите ввод или нажмите на /cancel для отмены'
            ),
            'en': fmt.text(
                'Invalid password "',
                fmt.hbold(msg),
                '". \nRe-enter your password or tap on /cancel for cancel'
            ),
        }
        return text

    private_key_incorrect = {
        'ru': fmt.text(
            'Не верный приватный ключ.\n',
            'Повторите ввод или нажмите на /cancel для отмены'
        ),
        'en': fmt.text(
            'Invalid private key.',
            'Re-enter your password or tap on /cancel for cancel'
        ),
    }

    # _______________________________________Change Language
    change_language = {
        'ru': fmt.text(
            fmt.hbold('Изменить язык')
        ),
        'en': fmt.text(
            fmt.hbold('Change language')
        )
    }
    change_language_done = {
        'ru': fmt.text(
            fmt.hbold('Язык успешно изменен')
        ),
        'en': fmt.text(
            fmt.hbold('Language changed successfully')
        )
    }

    # _______________________________________Change currency
    change_currency = {
        'ru': fmt.text(
            fmt.hbold('Изменить локальную валюту')
        ),
        'en': fmt.text(
            fmt.hbold('Change local currency')
        )
    }
    change_currency_done = {
        'ru': fmt.text(
            fmt.hbold('Локальная валюта успешно изменена')
        ),
        'en': fmt.text(
            fmt.hbold('Local currency changed successfully')
        )
    }
    # _______________________________________Special settings
    special_settings = {
        'ru': fmt.text(
            fmt.hbold('🔬 Особые настройки')
        ),
        'en': fmt.text(
            fmt.hbold('🔬 Special settings')
        )
    }
    # ______Delete Wallet
    delete_msg = {
        'ru': fmt.text(
            fmt.hbold('❌ Удаление кошелька ❌'),
            '\n\n',
            'Вы точно хотите удалить свой кошелёк?\n\n',
            fmt.hitalic('Удаление кошелька приведет к потере ваших средств. '
                        'Вы потверждаете, что несете отвественность.')
        ),
        'en': fmt.text(
            fmt.hbold('❌ Deleting the wallet ❌'),
            '\n\n',
            'Are you sure you want to delete your wallet?\n\n',
            fmt.hitalic(
                'Deleting your wallet will result in the loss of your funds. '
                'Вы потверждаете, что несете отвественность.')
        )
    }

    @staticmethod
    def password_invalid(cancel_msg='/cancel'):
        msg = {
            'ru': fmt.text(f"Не верный пароль. \nПовторите ввод или нажмите на {cancel_msg} для отмены."),
            'en': fmt.text(f"Invalid password. \nRetype or tap on {cancel_msg} for cancel"),
        }
        return msg

    password = {
        'ru': fmt.text(
            fmt.hbold('🔑 Введите пароль:')),
        'en': fmt.text(
            fmt.hbold('🔑 Enter password:')),
    }

    def new_wallet_after_del(self, private_key):
        message = {
            'ru': fmt.text(
                fmt.hbold('✨ Вы успешно удалили кошелёк. \n'
                          'Вам выдан новый пустой кошелёк Tron\n\n'),
                '💰 Ваш кошелёк: \n\n',
                fmt.hcode(self.user.wallet),
                '\n\n',
                '🔐 Ваш приватный ключ: \n\n',
                fmt.hspoiler(private_key),
                '\n\n📝 Обязательно сохраните свой приватный ключ для восстановления кошелька!\n\n',
                fmt.hbold('🔑 Пароль остается прежним\n\n'),
                'Вернуться в главное меню ➡️ /menu'
            ),
            'en': fmt.text(
                fmt.hbold('✨ You have successfully deleted your wallet. \n'
                          'You have been issued a new empty Tron wallet\n\n'),
                '💰 Your wallet: \n\n',
                fmt.hcode(self.user.wallet),
                '\n\n',
                '🔐 Your private key: \n',
                fmt.hspoiler(private_key),
                '\n\n📝 Be sure to save your private key to restore your wallet!\n\n',
                fmt.hbold('🔑 Password stays the same\n\n'),
                'Back to main menu ➡️ /menu'
            ),
        }
        return message[self.user.language]

    # ______Recovery Wallet
    recovery_msg = {
        'ru': fmt.text(
            fmt.hbold('❌ Восстановление кошелька ❌'),
            fmt.hunderline('\n⚩ с помощью приватного ключа'),
            '\n\n',
            'Вы точно хотите восстановить свой кошелёк?\n\n',
            fmt.hitalic('Восстановление вашего кошелька приведет к потере средств кошелька бота. '
                        'Вы потверждаете, что несете отвественность.')
        ),
        'en': fmt.text(
            fmt.hbold('❌ Recovery the wallet ❌'),
            fmt.hunderline('\n⚩ using a private key'),
            '\n\n',
            'Are you sure you want to recover your wallet?\n\n',
            fmt.hitalic(
                "Restoring your wallet will result in the loss of the bot's wallet funds. "
                'Вы потверждаете, что несете отвественность.')
        )
    }
    private_key = {
        'ru': fmt.text(
            fmt.hbold('🔐 Введите приватный ключ:')
        ),
        'en': fmt.text(
            fmt.hbold('🔐 Enter private key:')
        )
    }

    def new_wallet_after_rec(self):
        message = {
            'ru': fmt.text(
                fmt.hbold('✨ Кошелек успешно применен.\n\n'),
                '💰 Ваш кошелёк: \n\n',
                fmt.hcode(self.user.wallet),
                '\n\n',
                fmt.hbold('🔑 Пароль остается прежним\n\n'),
                'Вернуться в главное меню ➡️ /menu'
            ),
            'en': fmt.text(
                fmt.hbold('✨ Wallet applied successfully.\n\n'),
                '💰 Your wallet: \n\n',
                fmt.hcode(self.user.wallet),
                '\n\n',
                fmt.hbold('🔑 Password stays the same\n\n'),
                'Back to main menu ➡️ /menu'
            ),
        }
        return message[self.user.language]

    def private_key_invalid(self, cancel_msg='/cancel'):
        msg = {
            'ru': fmt.text(
                fmt.hbold("😔 Не удалось найти текущий кошелек в сети."),
                f"\n\nПовторите ввод или нажмите на {cancel_msg} для отмены."),
            'en': fmt.text(
                fmt.hbold("😔 Failed to find the current wallet on the network."),
                f"\n\nRetype or tap on {cancel_msg} for cancel"),
        }
        return msg[self.user.language]
