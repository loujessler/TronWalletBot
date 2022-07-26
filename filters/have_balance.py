from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api import quick_commands as commands
from utils.wallet_func.wallet_func import account_balance


class HaveBalance(BoundFilter):
    async def check(self, message: types.Message):
        user = await commands.select_user(message.from_user.id)
        balance = float(account_balance(user.wallet))
        amount = float(message.text.replace(',', '.'))
        print('Balance: ', balance)
        print('Amount: ', amount)
        ONE_TRON = 1000000
        result = (0.000001 <= amount) and (amount >= balance)
        print('Result: ', result)
        return result
