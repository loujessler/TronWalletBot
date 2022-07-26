from aiogram.dispatcher.filters.state import StatesGroup, State


class RecoveryWallet(StatesGroup):
    password = State()
    private_key = State()
