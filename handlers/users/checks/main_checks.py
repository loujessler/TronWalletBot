from aiogram.dispatcher import FSMContext
import re

from filters.check_address import CheckAddress
from keyboards.inline import ikb_menu_yes_no
from keyboards.inline.checks import ikb_menu_checks, ikb_check
from loader import dp, bot

from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, Message, ParseMode

from data.messages.checks_messages import ChecksMessages
from states.checks import DrawChecks
from utils.auxiliary_utilities import is_number
from utils.db_api import quick_commands as commands

from handlers.users.bot_start import edit_ls


# Добавляем возможность отмены, если пользователь передумал заполнять
from utils.wallet_func.wallet_func import address_check_func


@dp.message_handler(state='*', commands='cancel_drawcheck')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: Message, state: FSMContext):
    await message.delete()
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await checks_menu(message)


@dp.callback_query_handler(text='checks')
async def checks_menu(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(ChecksMessages(user).menu_msg(), call, ikb_menu_checks(user))


@dp.callback_query_handler(text='draw_check')
async def draw_check_func(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await edit_ls.edit_last_message(ChecksMessages(user).pre_draw_check_msg(), call)
    await DrawChecks.amount.set()


# Проверяем численность
@dp.message_handler(lambda message: (not is_number(message.text.replace(',', '.'))), state=DrawChecks.amount)
async def process_digit_invalid_check(message: Message):
    user = await commands.select_user(message.from_user.id)
    return await message.reply(ChecksMessages(user).cancel('/cancel_drawcheck'))


@dp.message_handler(state=DrawChecks.amount)
async def check(message: Message, state: FSMContext):
    user = await commands.select_user(message.from_user.id)
    amount = message.text.replace(',', '.')
    amount = amount.replace('.', '\.')
    await message.delete()
    await state.update_data(amount=amount)
    # await message.answer(ChecksMessages(user).check_msg(amount),
    #                      parse_mode="MarkdownV2",
    #                      reply_markup=ikb_check(user, ChecksMessages(user).check_msg(amount)))
    await edit_ls.edit_last_message(ChecksMessages(user).check_msg(amount),
                                    message,
                                    ikb_check(user, ChecksMessages(user).check_msg(amount)),
                                    "MarkdownV2")
    await state.finish()


# @dp.message_handler(state='*', commands='cancel')

# @dp.message_handler( text='/start')
@dp.message_handler(Text(startswith='@Testing_bot_aio_bot \n\n💸 ', ignore_case=True))
async def command_start(message: Message):
    msg_split = [message.text.split(' ')[6], message.text.split(' ')[10], ]
    await message.delete()
    user = await commands.select_user(message.from_user.id)
    print(address_check_func(msg_split[1]))
    if address_check_func(msg_split[1]) is True:
        await edit_ls.edit_last_message(ChecksMessages(user).ask_msg_for_send(msg_split),
                                        message,
                                        ikb_menu_yes_no(user, 'send_checks'))
    else:
        await edit_ls.edit_last_message(ChecksMessages(user).address_not_found(msg_split[1]),
                                        message)


# @dp.callback_query_handler(text='yessend_checks')
# async def yes_checks_command(call: CallbackQuery):
#
#     user = await commands.select_user(call.from_user.id)
#     await edit_ls.edit_last_message(ChecksMessages(user).ask_msg_for_send(msg_split),
#                                     call,
#                                     ikb_menu_yes_no(user, 'send_checks'))


