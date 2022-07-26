import aiogram.utils.markdown as fmt

from data.currencies import currencies
from data.languages import languages


class ChecksMessages:
    def __init__(self, user):
        self.user = user

    def menu_msg(self):
        msg = {
            'ru': fmt.text(
                fmt.hbold('🧾️ Чеки\n\n'),
            ),
            'en': fmt.text(
                fmt.hbold('🧾 Checks\n\n'),
            )
        }
        return msg[self.user.language]

    def pre_draw_check_msg(self):
        msg = {
            'ru': fmt.text(
                fmt.hbold('🖋 Выписать чек\n\n'),
                fmt.hitalic('Вы можете выписать чек пользователю для оплаты\n\n'),
                'Введите сумму для оплаты'
            ),
            'en': fmt.text(
                fmt.hbold('🖋 Draw a check\n\n'),
                fmt.hitalic('You can write a check to the user for payment\n\n'),
                'Enter the amount to pay'
            )
        }
        return msg[self.user.language]

    def draw_check_msg(self):
        msg = {
            'ru': fmt.text(
                fmt.hbold('🪄 Подготовка чека оплаты\n\n'),
                fmt.hitalic('Вы можете выписать чек на определенную сумму пользователю для оплаты\n\n'),
                f'Введите сумму для оплаты'
            ),
            'en': fmt.text(
                fmt.hbold('🪄 Draw a check\n\n'),
                fmt.hitalic('You can write a check to the user for payment\n\n'),
                'Enter the amount to pay'
            )
        }
        return msg[self.user.language]

    def check_msg(self, amount):
        msg = {
            'ru': (
                f'\n\n💸 **Чек оплаты**\n\n'
                f'Оплата на сумму {amount} TRX\n\n'
                f'Кошелек для оплаты:\n '
                f'`{self.user.wallet}` '
            ),
            'en': (
                f'\n\n💸 **Draw a check**\n\n'
                f'Payment for the amount {amount} TRX\n\n'
                f'Wallet for payment:\n '
                f'`{self.user.wallet}` '
            )
        }
        return msg[self.user.language]

    def check_msg_resend(self):
        msg = {
            'ru': f'\n\n__Чтобы совершить автоматическую оплату отправьте текущий чек боту__ ',
            'en': f'\n\n__To make an automatic payment - send the current check to the bot__'
        }
        return msg[self.user.language]

    def ask_msg_for_send(self, data_msg):
        msg = {
            'ru': fmt.text(
                fmt.hbold('✅ Потверждение об отправке\n\n'),
                f'Вы действительно хотите отправить {data_msg[0]} TRX\n\n',
                f'На кошелёк:\n',
                fmt.hcode(data_msg[1])
            ),
            'en': fmt.text(
                fmt.hbold('✅ Send transaction\n\n'),
                f'Do you really want to send {data_msg[0]} TRX\n\n',
                f'To wallet:\n',
                fmt.hcode(data_msg[1])
            )
        }
        return msg[self.user.language]

    def address_not_found(self, wallet):
        msg = {
            'ru': fmt.text(
                fmt.hbold('Мы не нашли текущий адрес:  '),
                fmt.hcode(wallet),
                '\n в сети TRON\n\n',
                'Перейти в меню /menu'
            ),
            'en': fmt.text(
                fmt.hbold("We didn't find the current address:"),
                fmt.hcode(wallet),
                '\n in TRON network',
                'Return to menu /menu'
            ),
        }
        return msg[self.user.language]

    def cancel(self, cancel_msg='/cancel'):
        msg = {
            'ru': fmt.text(f"Напиши число или нажмите на {cancel_msg} для отмены"),
            'en': fmt.text(f"Write a number or tap on {cancel_msg} for cancel"),
        }
        return msg[self.user.language]
