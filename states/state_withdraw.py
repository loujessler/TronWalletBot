from aiogram.dispatcher.filters.state import StatesGroup, State


class Withdraw_state(StatesGroup):
    balance = State()
    password = State()
    amount = State()
    wallet = State()
    answer = State()