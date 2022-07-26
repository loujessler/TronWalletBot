from aiogram import Dispatcher

from .private_chat import IsPrivate
from .have_balance import HaveBalance
from .have_db import HaveInDb
from .password_invalid import IsCorrectPassword
from .private_key_invalid import IsCorrectPrivateKey


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
