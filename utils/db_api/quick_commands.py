from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemes.user import User


async def add_user(user_id: int,
                   first_name: str,
                   last_name: str,
                   username: str,
                   wallet: str,
                   status: str,
                   private_key: str,
                   language: str,
                   currency: str):
    try:
        user = User(user_id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    status=status,
                    wallet=wallet,
                    private_key=private_key,
                    language=language,
                    currency=currency)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def update_private_key(user_id, private_key):
    user = await select_user(user_id)
    await user.update(private_key=private_key).apply()


async def update_language(user_id, language):
    user = await select_user(user_id)
    await user.update(language=language).apply()


async def update_currency(user_id, currency):
    user = await select_user(user_id)
    await user.update(currency=currency).apply()


async def delete_wallet(user_id, wallet, private_key):
    user = await select_user(user_id)
    await user.update(wallet=wallet).apply()
    await user.update(private_key=private_key).apply()
