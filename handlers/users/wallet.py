from aiogram.dispatcher import FSMContext

from filters import HaveInDb
from loader import dp
from aiogram import types
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Command

from data.messages.messages import Messages
from utils.db_api import quick_commands as commands
from keyboards.inline import ikb_menu_my_wallet
from utils.set_bot_commands import set_start_commands

from utils.wallet_func.wallet_func import account_balance

# from aiogram import html
from aiogram.contrib.middlewares.i18n import I18nMiddleware


async def wallet_func(aiotype, state):
    await aiotype.delete()
    user = await commands.select_user(aiotype.from_user.id)
    try:
        balance = account_balance(user.wallet)
    except Exception:
        balance = 0
    await state.update_data(balance=balance)
    await aiotype.answer(Messages.my_wallet(user, balance)[user.language],
                         reply_markup=ikb_menu_my_wallet(user), parse_mode='HTML')


@dp.message_handler(HaveInDb(True), Command('wallet'))
async def send_wallet_menu_command(message: types.Message, state: FSMContext):
    await wallet_func(message, state)


# await message.delete()
    # user = await commands.select_user(message.from_user.id)
    # try:
    #     balance = account_balance(user.wallet)
    # except Exception:
    #     balance = 0
    # await state.update_data(balance=balance)
    # await message.answer(Messages.my_wallet(balance)[user.language],
    #                      reply_markup=ikb_menu_my_wallet(user), parse_mode='HTML')
