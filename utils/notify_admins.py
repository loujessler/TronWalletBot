import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            text = "The bot is up and running"
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
