from aiogram.types import CallbackQuery
from data.messages.withdraw_msg import Withdraw
from keyboards.inline import ikb_menu_back_to_wallet, ikb_menu_zero_balance
from loader import dp
from utils.wallet_func.wallet_func import resource_tron
from utils.db_api import quick_commands as commands


@dp.callback_query_handler(text='bandwidth')
async def resource_menu(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    try:
        try:
            resource = resource_tron(user.wallet)
            net_limit = resource['freeNetLimit']
            if 'freeNetUsed' in resource:
                net_left = resource['freeNetLimit'] - resource['freeNetUsed']
            else:
                net_left = 1500
            await call.message.edit_text(Withdraw.resource_msg(net_limit, net_left)[user.language],
                                         parse_mode='HTML')
            await call.message.edit_reply_markup(ikb_menu_back_to_wallet(user))
        except Exception:
            await call.message.edit_text(Withdraw.withdraw_zero_wallet[user.language],
                                         reply_markup=ikb_menu_zero_balance(user))
    except Exception as ex:
        await call.message.answer(f'Error: {ex}')
