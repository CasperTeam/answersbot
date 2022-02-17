from pyrogram import Client, filters
from pyrogram.types import Message
from bs4 import BeautifulSoup
from bot import COMMM_AND_PRE_FIX, HELP_COMMAND
from bot.bot import Bot


@Bot.on_message(
    filters.command("sheet", COMMM_AND_PRE_FIX)
)
async def sheet(client: Bot, message: Message):
    await message.reply_text("https://docs.google.com/spreadsheets/d/1Iuz971A-HmOQBf3y005XBO3XCEpsJZly2GL8Cc6Gar0/edit?usp=drivesdk")

    
@Bot.on_message(
    filters.command("start")
)
async def sheet(client: Bot, message: Message):
    DEFAULT_START_TEXT = (
    "Hi. ☺️\n"
    "Thank you for using me.\n\n"
    "This is abot to contact admins! \n\n\n"
    "Google Sheets Link -> /sheet \n\n\n"
    "**Rules for using this bot:** "
    "1. Ask your question Directly "
    "2. dont edit or delete messages "
    "3. **Dont Spam!** \n\n\n"
    "New Features Will Come bu for next batch."
    "ℹ️ Thanks 😍 for using this bot❗️❣️"
    )  
    await message.reply_text(DEFAULT_START_TEXT, reply_markup="md")

    
