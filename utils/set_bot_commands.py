from aiogram import types
from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat

from utils.db_api import quick_commands as commands

texts = {
    'menu': {
        'ru': 'Главное меню',
        'en': 'Main menu',
    },
    'wallet': {
        'ru': '💰 Мой кошелек',
        'en': '💰 My wallet',
    },
    'cheques': {
        'ru': '🧾 Чеки',
        'en': '🧾 Cheques',
    },
    'settings': {
        'ru': '⚙️ Настройки',
        'en': '⚙️ Settings',
    },
    'help': {
        'ru': '💬 Помощь',
        'en': '💬 Help',
    },
}


async def set_default_commands(bot):
    return await bot.set_my_commands(
        commands=[
            types.BotCommand('start', 'Start'),
            # types.BotCommand('menu', 'Main menu'),
            # types.BotCommand('wallet', '💰 My wallet'),
            # types.BotCommand('cheques', '🧾 Cheques'),
            # types.BotCommand('settings', '⚙️ Settings'),
            # types.BotCommand('help', '💬 Help'),
        ],
        scope=BotCommandScopeDefault(),
    )


async def set_start_commands(bot, chat_id, language):
    text_commands = {
        'ru': [
            types.BotCommand('menu', 'Главное меню'),
            types.BotCommand('wallet', '💰 Мой кошелек'),
            types.BotCommand('cheques', '🧾 Чеки'),
            types.BotCommand('settings', '⚙️ Настройки'),
            types.BotCommand('help', '💬 Помощь'),
        ],
        'en': [
            types.BotCommand('menu', 'Main menu'),
            types.BotCommand('wallet', '💰 My wallet'),
            types.BotCommand('cheques', '🧾 Cheques'),
            types.BotCommand('settings', '⚙️ Settings'),
            types.BotCommand('help', '💬 Help'),
        ]
    }
    for language_code, commands in text_commands.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )
