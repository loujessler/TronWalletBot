from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteWallet(StatesGroup):
    password = State()
