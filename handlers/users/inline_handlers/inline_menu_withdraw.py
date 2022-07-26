from aiogram.dispatcher import FSMContext

from data.messages.withdraw_msg import Withdraw
from filters import HaveBalance, IsCorrectPassword
from filters.check_address import CheckAddress
from handlers.users.bot_start import edit_ls
from handlers.users.wallet import wallet_func
from loader import dp
from aiogram import types

from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text

from states.state_withdraw import Withdraw_state
from utils.auxiliary_utilities import is_number
from utils.db_api import quick_commands as commands
from keyboards.inline import ikb_menu_back_to_wallet, ikb_menu_zero_balance, ikb_menu_yes_no, ikb_link_transaction

from utils.wallet_func.wallet_func import account_balance, send_tron, check_fee


# Добавляем возможность отмены, если пользователь передумал заполнять
@dp.message_handler(state='*', commands='cancel_withdraw')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await wallet_func(message, state)


# _______________Original
@dp.callback_query_handler(text='withdraw')
async def withdraw_menu(call: CallbackQuery, state: FSMContext):
    user = await commands.select_user(call.from_user.id)
    data = await state.get_data()
    try:
        balance = data.get('balance')
        if balance is None:
            balance = account_balance(user.wallet)
        await state.finish()
        if float(balance) > 0.1:
            await call.message.edit_text(Withdraw.withdraw(balance)[user.language], parse_mode='HTML')
            await Withdraw_state.amount.set()
        else:
            await call.message.edit_text(
                Withdraw.withdraw_zero_wallet[user.language],
                reply_markup=ikb_menu_zero_balance(user)
            )
    except Exception as ex:
        await call.message.edit_text(
            f'Error: {ex}',
            reply_markup=ikb_menu_back_to_wallet(user)
        )
# _______________Original


# ________test
# @dp.callback_query_handler(text='withdraw')
# async def withdraw_menu(call: CallbackQuery, state: FSMContext):
#     user = await commands.select_user(call.from_user.id)
#
#     data = await state.get_data()
#     try:
#         balance = data.get('balance')
#         if balance is None:
#             balance = account_balance(user.wallet)
#         await state.finish()
#         if float(balance) > 0.1:
#             await call.message.answer(Withdraw.password[user.language], parse_mode='HTML')
#             await state.update_data(balance=balance)
#             await Withdraw_state.password.set()
#             # await call.message.edit_text(Withdraw.withdraw(balance)[user.language], parse_mode='HTML')
#             # await Withdraw_state.amount.set()
#         else:
#             await call.message.edit_text(
#                 Withdraw.withdraw_zero_wallet[user.language],
#                 reply_markup=ikb_menu_zero_balance(user)
#             )
#     except Exception as ex:
#         await call.message.edit_text(
#             f'Error: {ex}',
#             reply_markup=ikb_menu_back_to_wallet(user)
#         )
#
#
# # Проверяем пароль
# @dp.message_handler(IsCorrectPassword(), state=Withdraw_state.password)
# async def process_password_invalid(message: types.Message):
#     user = await commands.select_user(message.from_user.id)
#     return await message.reply(Withdraw.password_invalid[user.language])
#
#
# @dp.message_handler(state=Withdraw_state.password)
# async def write_password(message: types.Message, state: FSMContext):
#     user = await commands.select_user(message.from_user.id)
#     data = await state.get_data()
#     balance = data.get('balance')
#     password = message.text
#     await message.answer(Withdraw.withdraw(balance)[user.language], parse_mode='HTML')
#     await state.update_data(password=password)
#     await state.update_data(balance=balance)
#     await Withdraw_state.amount.set()


# ________test


# ________Original


# Проверяем численность
@dp.message_handler(lambda message: (not is_number(message.text.replace(',', '.'))), state=Withdraw_state.amount)
async def process_digit_invalid(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    return await message.reply(Withdraw.cancel[user.language])


# (Messages.my_wallet(balance), reply_markup=ikb_menu_my_wallet, parse_mode=ParseMode.MARKDOWN)


# Проверяем допустимый счёт
@dp.message_handler(HaveBalance(),
                    state=Withdraw_state.amount)
async def process_balance_invalid(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    balance = account_balance(user.wallet)
    return await message.reply(Withdraw.balance_invalid(balance)[user.language])


@dp.message_handler(state=Withdraw_state.amount)
async def withdraw_state_amount(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)
    amount = message.text.replace(',', '.')
    await message.delete()
    await state.update_data(amount=amount)

    await edit_ls.edit_last_message(Withdraw.state_amount(amount)[user.language], message)
    # await message.answer(Withdraw.state_amount(amount)[user.language])
    await Withdraw_state.wallet.set()


@dp.message_handler(CheckAddress(), state=Withdraw_state.wallet)
async def check_wallet(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    wallet = str(message.text)
    return await message.answer(Withdraw.check_wallet_msg(wallet)[user.language], parse_mode='HTML')


@dp.message_handler(state=Withdraw_state.wallet)
async def withdraw_state_wallet(message: types.Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)
    wallet = message.text
    await state.update_data(wallet=wallet)
    data = await state.get_data()
    amount = data.get('amount')
    wallet = data.get('wallet')
    await message.delete()
    await edit_ls.edit_last_message(Withdraw.state_wallet(user, amount, wallet)[user.language],
                                    message,
                                    ikb_menu_yes_no(user))
    # await message.answer(
    #     Withdraw.state_wallet(amount, wallet)[user.language],
    #     reply_markup=ikb_menu_yes_no(user),
    #     parse_mode='HTML'
    # )


# ________Original

# ________test
# @dp.callback_query_handler(text='yes', state=Withdraw_state.wallet)
# async def yes(call: CallbackQuery, state: FSMContext):
#     one_tron = 1000000
#     user = await commands.select_user(call.from_user.id)
#     data = await state.get_data()
#     print(data)
#     amount = int(float(data.get('amount')) * one_tron)
#     wallet = data.get('wallet')
#     try:
#         send = send_tron(user.wallet, wallet, amount, user.private_key, data.get('password'))
#         tx_id = send['id']
#         ikb_link = await ikb_link_transaction(tx_id, user)
#         await call.message.edit_text(Withdraw.withdraw_completed(amount, one_tron, wallet)[user.language],
#                                      parse_mode='HTML'
#                                      )
#         await call.message.edit_reply_markup(reply_markup=ikb_link)
#         await state.finish()
#     except Exception as ex:
#         await call.message.edit_text(Withdraw.withdraw_invalid(ex)[user.language])
#         await call.message.edit_reply_markup(reply_markup=ikb_menu_back_to_wallet(user))
#         await state.set_state(Withdraw_state.password)
#     await state.finish()
#
#
# @dp.callback_query_handler(text='no', state=Withdraw_state.wallet)
# async def no(call: CallbackQuery, state: FSMContext):
#     user = await commands.select_user(call.from_user.id)
#     await call.message.edit_text(Withdraw.withdraw_cancel[user.language])
#     await call.message.edit_reply_markup(reply_markup=ikb_menu_back_to_wallet(user))
#     await state.finish()
# ________test

# _____________Original
@dp.callback_query_handler(text='yes', state=Withdraw_state.wallet)
async def write_password(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(Withdraw.password[user.language],
                                    call)
    # await call.message.answer(Withdraw.password[user.language], parse_mode='HTML')
    await Withdraw_state.password.set()


# Проверяем пароль
@dp.message_handler(IsCorrectPassword(), state=Withdraw_state.password)
async def process_password_invalid(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    return await message.answer(Withdraw.password_invalid[user.language])


@dp.message_handler(state=Withdraw_state.password)
async def yes(message: types.Message, state: FSMContext):
    # Testing password
    password = message.text
    await state.update_data(password=password)
    #################
    await message.delete()
    one_tron = 1000000
    user = await commands.select_user(message.from_user.id)
    data = await state.get_data()
    amount = int(float(data.get('amount')) * one_tron)
    wallet = data.get('wallet')
    try:
        # ______________ORIGINAL
        send = send_tron(user.wallet, wallet, amount, user.private_key, data.get('password'))
        tx_id = send['id']
        ikb_link = await ikb_link_transaction(tx_id, user)
        await edit_ls.edit_last_message(Withdraw.withdraw_completed(amount, one_tron, wallet)[user.language],
                                        message,
                                        ikb_link)
        # ______________ORIGINAL
        # ______________TEST FEE
        # check = check_fee(user.wallet, wallet, amount)
        # print(check)
        # await message.answer(check)
        # ______________TEST FEE
        await state.finish()
    except Exception as ex:
        await message.answer(Withdraw.withdraw_invalid(ex)[user.language],
                             reply_markup=ikb_menu_back_to_wallet(user)
                             )
        await state.set_state(Withdraw_state.password)
    await state.finish()


@dp.callback_query_handler(text='no', state=Withdraw_state.wallet)
async def no(call: CallbackQuery, state: FSMContext):
    user = await commands.select_user(call.from_user.id)
    await call.message.edit_text(Withdraw.withdraw_cancel[user.language])
    await call.message.edit_reply_markup(reply_markup=ikb_menu_back_to_wallet(user))
    await state.finish()
