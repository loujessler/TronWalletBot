

async def on_startup(dp):

    import filters
    filters.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup
    await on_startup(dp)
    # await db.gino.drop_all()
    await db.gino.create_all()

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(bot)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    from loader import shutdown, bot

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=shutdown)

# import logging
#
# from aiogram import Bot, types, Dispatcher
# from aiogram.utils import executor
# # from aiogram.dispatcher import Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
#
# from data.config import API_TOKEN
#
# logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
#                     level=logging.DEBUG)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot, storage=MemoryStorage())
# dp.middleware.setup(LoggingMiddleware())
#
#
# ################################
#
#
# ################################
#
# if __name__ == '__main__':
#     from handlers import dp, shutdown
#
#     executor.start_polling(dp, on_shutdown=shutdown)
