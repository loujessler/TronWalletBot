import aiogram.types
from aiogram.types import ParseMode


class EditLastMessage:
    def __init__(self, bot):
        self.bot = bot

    async def edit_last_message(self, edit_message, aio_type, ikb=None, parse_mode='HTML'):
        i = 0
        while True:
            if i > 10:
                await self.bot.send_message(aio_type.from_user.id,
                                            edit_message,
                                            reply_markup=ikb,
                                            parse_mode=str(parse_mode)
                                            )
                break
            else:
                try:
                    try:
                        message_id = (aio_type.message_id - i)
                    except:
                        message_id = (aio_type.message.message_id - i)
                    await self.bot.edit_message_text(edit_message,
                                                     aio_type.from_user.id,
                                                     message_id,
                                                     parse_mode=str(parse_mode))
                    break
                except Exception:
                    i += 1
                    pass
        if ikb is not None:
            try:
                message_id = (aio_type.message_id - i)
            except:
                message_id = (aio_type.message.message_id - i)
            await self.bot.edit_message_reply_markup(aio_type.from_user.id,
                                                     message_id,
                                                     reply_markup=ikb)
