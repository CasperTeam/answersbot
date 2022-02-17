from pyrogram import Client, filters
from pyrogram.types import Message
from bs4 import BeautifulSoup
from bot import COMMM_AND_PRE_FIX, HELP_COMMAND
from bot.bot import Bot


@Bot.on_message(
    filters.command("sheet", COMMM_AND_PRE_FIX)
)
async def sheet(client: Bot, message: Message):
    Message.reply = ("https://docs.google.com/spreadsheets/d/1Iuz971A-HmOQBf3y005XBO3XCEpsJZly2GL8Cc6Gar0/edit?usp=drivesdk")

    
