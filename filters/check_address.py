from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.wallet_func.wallet_func import address_check_func


class CheckAddress(BoundFilter):
    async def check(self, message: types.Message):
        wallet = message.text
        try:
            address = address_check_func(wallet)
            return not address
        except Exception:
            return False
