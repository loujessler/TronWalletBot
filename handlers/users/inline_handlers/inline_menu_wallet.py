from aiogram.dispatcher import FSMContext

from filters import HaveInDb
from loader import dp
from aiogram.dispatcher.filters import Command

from aiogram.types import CallbackQuery

from data.messages.messages import Messages

from utils.db_api import quick_commands as commands
from keyboards.inline import ikb_menu_my_wallet, ikb_menu_back_to_wallet
from utils.set_bot_commands import set_start_commands

from utils.wallet_func.wallet_func import account_balance


@dp.callback_query_handler(text='back to wallet')
@dp.callback_query_handler(text='my wallet')
async def wallet_menu(call: CallbackQuery, state: FSMContext):
    user = await commands.select_user(call.from_user.id)
    try:
        balance = account_balance(user.wallet)
    except Exception:
        balance = 0
    await state.update_data(balance=balance)
    await call.message.edit_text(Messages.my_wallet(user, balance)[user.language], parse_mode='HTML')
    await call.message.edit_reply_markup(ikb_menu_my_wallet(user))


@dp.callback_query_handler(text='deposit')
async def deposit_menu(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await call.message.edit_text(Messages.deposit_wallet(user.wallet)[user.language], parse_mode="HTML")
    await call.message.edit_reply_markup(ikb_menu_back_to_wallet(user))
