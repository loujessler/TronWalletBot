from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api import quick_commands as commands
from utils.encryption import decrypt_xor
from utils.wallet_func.wallet_func import send_tron


class DecryptXorPrivate:
    def __init__(self, psw):
        self.psw = psw

    def func(self, priv):
        print(priv)
        return decrypt_xor(priv, self.psw)


class IsCorrectPassword(BoundFilter):
    async def check(self, message: types.Message):
        d = DecryptXorPrivate(message.text)
        user = await commands.select_user(message.from_user.id)
        len_private = len(user.private_key)
        # print('Private key: ',
        #       d.func(user.private_key[3:len_private - 3])[3:6] == user.private_key[:3],
        #       d.func(user.private_key[3:len_private - 3])[
        #       len(d.func(user.private_key[3:len_private - 3])) - 6:
        #       len(d.func(user.private_key[3:len_private - 3])) - 3
        #       ] == user.private_key[len_private - 3:]
        #       )
        # print(d.func(user.private_key[3:len_private - 3])[3:6] == user.private_key[:3] ,
        #         d.func(user.private_key[3:len_private - 3])[
        #         len(d.func(user.private_key[3:len_private - 3])) - 6:
        #         len(d.func(user.private_key[3:len_private - 3])) - 3
        #         ] == user.private_key[len_private - 3:])
        if d.func(user.private_key[3:len_private - 3])[3:6] == user.private_key[:3] and \
                d.func(user.private_key[3:len_private - 3])[
                len(d.func(user.private_key[3:len_private - 3])) - 6:
                len(d.func(user.private_key[3:len_private - 3])) - 3
                ] == user.private_key[len_private - 3:len_private]:

            # send = send_tron(user.wallet, 'TFnTfrybSWGFu83BSgJxp14jZ4Jywu1FCX', 0, user.private_key, message.text) # Original Net
            send = send_tron(user.wallet, 'TMWXhuxiT1KczhBxCseCDDsrhmpYGUcoA9', 0, user.private_key,
                             message.text)  # Test Net
            result = str(send) == 'Contract validate error : Amount must be greater than 0.' or str(
                send) == 'Contract validate error : account does not exist'
            return not result
        else:
            return True

# _________________ORIGINAL
# class IsCorrectPassword(BoundFilter):
#     async def check(self, message: types.Message):
#         d = DecryptXorPrivate(message.text)
#         user = await commands.select_user(message.from_user.id)
#         send = send_tron(user.wallet, 'TFnTfrybSWGFu83BSgJxp14jZ4Jywu1FCX', 0, user.private_key, message.text)
#         result = str(send) == 'Contract validate error : Amount must be greater than 0.'
#         return not result
