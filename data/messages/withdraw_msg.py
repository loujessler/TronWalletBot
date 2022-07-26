import aiogram.utils.markdown as fmt

from utils.wallet_func.wallet_func import check_fee, resource_tron


class Withdraw:
    @staticmethod
    def withdraw(balance):
        message = {
            'ru': fmt.text(fmt.hbold(f'⤴️ Вывод средств\n'), f'\n',
                           f'Ваш баланс ',
                           balance,
                           '  TRX', f'\n',
                           'Укажите сумму для вывода:'),
            'en': fmt.text(fmt.hbold(f'⤴️ Withdrawals\n'), f'\n',
                           f'Your balance ',
                           balance,
                           '  TRX', f'\n',
                           'Specify the amount to withdraw:'),
        }
        return message

    withdraw_zero_wallet = {
        'ru': fmt.text('На вашем балансе недостаточно средств. Пожалуйста, пополните ваш кошелек'),
        'en': fmt.text('There are not enough funds on your balance. Please top up your wallet'),
    }

    cancel = {
        'ru': fmt.text("Напиши число или нажмите на /cancel_withdraw для отмены"),
        'en': fmt.text("Write a number or tap on /cancel_withdraw for cancel"),
    }

    password = {
        'ru': fmt.text(
            fmt.hbold('🔑 Введите пароль:')),
        'en': fmt.text(
            fmt.hbold('🔑 Enter password:')),
    }

    @staticmethod
    def balance_invalid(balance):
        msg = {
            'ru': fmt.text('Недостаточно средств. Ваш баланс ',
                           balance,
                           f'\nДля отмены нажмите на /cancel_withdraw'),
            'en': fmt.text('Insufficient funds. Your balance ',
                           balance,
                           f'\nFor cancel tap on /cancel_withdraw'),
        }
        return msg

    @staticmethod
    def state_amount(amount):
        msg = {
            'ru': fmt.text(
                'Вы хотите вывести ',
                amount,
                f' TRX.\n\nУкажите адрес кошелька TRX: \n'
            ),
            'en': fmt.text(
                'You want to withdraw ',
                amount,
                f' TRX.\n\nEnter wallet address TRX: \n'
            ),
        }
        return msg

    @staticmethod
    def check_wallet_msg(wallet):
        msg = {
            'ru': fmt.text(
                fmt.hbold(f'Не найдет такой адресс в сети TRON: \n'),
                fmt.hcode(wallet),
                f'\n\nДля отмены нажмите /cancel_withdraw'
            ),
            'en': fmt.text(
                fmt.hbold(f"Can't find this address on the network TRON: \n"),
                fmt.hcode(wallet),
                f'\n\nFor cancel tap on /cancel_withdraw'
            ),
        }
        return msg

    @staticmethod
    def state_wallet(user, amount, wallet):
        def calculate_fee(user, wallet, amount):
            fee = check_fee(user, wallet, amount)
            resource = resource_tron(user.wallet)
            if 'freeNetUsed' in resource:
                net_left = resource['freeNetLimit'] - resource['freeNetUsed']
            else:
                net_left = 1500
            if fee > net_left:
                return fee/1000
            else:
                return 0
        msg = {
            'ru': fmt.text(
                fmt.hbold('Вы хотите вывести '),
                amount,
                fmt.hbold('  TRX'),
                f'\n\nКомиссия составит ≈ ',

                calculate_fee(user, wallet, amount),

                fmt.hbold('  TRX'),
                f'\n\nНа адрес: \n\n',
                fmt.hcode(wallet),
                f'\n'
            ),
            'en': fmt.text(
                fmt.hbold('You want to withdraw '),
                amount,
                fmt.hbold('  TRX'),
                f'\nTo the address: \n\n',
                fmt.hcode(wallet),
                f'\n'
            ),
        }
        return msg

    password_invalid = {
        'ru': fmt.text(f"Не верный пароль. \nПовторите ввод или нажмите на /cancel_withdraw для отмены."),
        'en': fmt.text(f"Invalid password. \nRetype or tap on /cancel_withdraw for cancel"),
    }

    @staticmethod
    def withdraw_completed(amount, one_tron, wallet):
        msg = {
            'ru': fmt.text(
                fmt.hbold('Вывод прошел успешно\n\n'),
                'Сумма ',
                float(amount) / one_tron,
                '  TRX\n\n',
                'На адрес: ',
                fmt.hcode(wallet), f'\n\n'),
            'en': fmt.text(
                fmt.hbold('Withdrawal was successful\n\n'),
                'Amount ',
                float(amount) / one_tron,
                '  TRX\n\n',
                'To the address: ',
                fmt.hcode(wallet), f'\n\n'),
        }
        return msg

    @staticmethod
    def withdraw_invalid(ex):
        msg = {
            'ru': fmt.text(f'Не удалось совершить перевод\n\n'
                           'Ошибка: ',
                           ex),
            'en': fmt.text(f'Failed to complete the transaction\n\n'
                           'Error: ',
                           ex),
        }
        return msg

    withdraw_cancel = {
        'ru': fmt.text('Вы отменили транзакцию'),
        'en': fmt.text('You canceled the transaction'),
    }

# resource menu

    @staticmethod
    def resource_msg(net_limit, net_left):
        msg = {
            'ru': fmt.text(
                '🚀️',
                fmt.hbold(' Пропускная способность'),
                f'\n\nОсталось: ',
                fmt.hbold(net_left),
                fmt.hitalic('/'),
                fmt.hitalic(net_limit),
                ' 🚀'
            ),
            'en': fmt.text(
                '🚀️',
                fmt.hbold(' Bandwidth'),
                f'\n\nLeft: ',
                fmt.hbold(net_left),
                fmt.hitalic('/'),
                fmt.hitalic(net_limit),
                ' 🚀'
            ),
        }
        return msg
