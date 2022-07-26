
from aiogram import Bot, types, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from utils.db_api.db_gino import db
from data import config
from utils.edit_last_message import EditLastMessage


import logging

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    # level=logging.INFO,
                    level=logging.DEBUG,
                    )

bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())

# edit_ls = EditLastMessage(bot)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


__all__ = ['bot', 'db', 'storage', 'dp']

################################


################################

# if __name__ == '__main__':
#     from handlers import dp, shutdown
#
#     executor.start_polling(dp, on_shutdown=shutdown)
