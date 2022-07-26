from aiogram.dispatcher.filters.state import StatesGroup, State


class DrawChecks(StatesGroup):
    amount = State()
