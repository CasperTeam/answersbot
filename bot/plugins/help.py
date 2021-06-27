from pyrogram import Client, filters
from pyrogram.types import Message
from bs4 import BeautifulSoup
from bot import AUTH_CHANNEL, COMMM_AND_PRE_FIX, HELP_COMMAND
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.sql.users_sql import get_chats


@Bot.on_message(
    filters.command(HELP_COMMAND, COMMM_AND_PRE_FIX)
)
async def num_start_message(client: Bot, message: Message):
    reply = hello
