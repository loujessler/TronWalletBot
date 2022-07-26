import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config.POSTGRES_URL)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(143, 'Vlad', 'TAemEqKZKR5YLdY98yHfZ1XahgyPRioJy5',
                            '21ee24d40e5e6993faac3eb139966dca46b629f26b0faaeb69b78bc72c625026', 'Alex')
    await commands.add_user(13, 'Dima', 'TAemEqKZKR5YLdY98yHfZ1XahgyPRioJy5',
                            '21ee24d40e5e6993faac3eb139966dca46b629f26b0faaeb69b78bc72c625026', 'Alex')

    users = await commands.select_all_users()
    print("Выбрать всех: ", users)

    count = await commands.count_users()
    print("Посчитать кол-во:", count)

    user = await commands.select_user(13)
    print("Выбрать чела: ", user)

    await commands.update_user_name(13, 'new Dima name')

    user = await commands.select_user(13)
    print("Выбрать чела: ", user)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
