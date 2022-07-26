from loader import dp
from aiogram.types import CallbackQuery, ParseMode

from data.messages.messages import Messages
from keyboards.inline import ikb_menu, ikb_menu_my_wallet
from utils.db_api import quick_commands as commands
from utils.wallet_func.wallet_func import account_balance


@dp.callback_query_handler(text='back')
async def send_message(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await call.message.edit_text(Messages.menu[user.language], parse_mode='HTML')
    await call.message.edit_reply_markup(ikb_menu(user))

