from aiogram.dispatcher.filters.state import StatesGroup, State


class Change_password(StatesGroup):
    last_password = State()
    password = State()
    reply_password = State()
    private_key = State()