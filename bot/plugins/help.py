from pyrogram import Client, filters
from pyrogram.types import Message
from bs4 import BeautifulSoup
from bot import COMMM_AND_PRE_FIX, HELP_COMMAND
from bot.bot import Bot


@Bot.on_message(
    filters.command(HELP_COMMAND, COMMM_AND_PRE_FIX)
)
async def num_help_message(client: Bot, message: Message):
    Message.reply = ("no help for now check next week")
