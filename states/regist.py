from aiogram.dispatcher.filters.state import StatesGroup, State


class Regist(StatesGroup):
    language = State()
    password = State()
    reply_password = State()
    msg = State()