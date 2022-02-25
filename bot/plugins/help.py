from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bs4 import BeautifulSoup
from bot import COMMM_AND_PRE_FIX, HELP_COMMAND
from bot.bot import Bot


@Bot.on_message(
    filters.command("sheet", COMMM_AND_PRE_FIX)
)
async def sheet(client: Bot, message: Message):
    await message.reply_text("https://ourclg.tech/sheet.php",disable_web_page_preview=True)

    
@Bot.on_message(
    filters.command("start")
)
async def start(client: Bot, message: Message):
    B = InlineKeyboardMarkup(InlineKeyboardButton[text="Sheets",url="https://ourclg.tech/sheet.php"])
    DEFAULT_START_TEXT = (
    "Hi. ☺️\n"
    "Thank you for using me.\n\n"
    "This is abot to contact admins! \n\n\n"
    "Google Sheets Link -> /sheet \n\n\n"
    "**Rules for using this bot:\n\n** "
    "1. Ask your question Directly \n"
    "2. dont edit or delete messages\n"
    "3. **Dont Spam!** \n\n\n"
    "New Features Will Come bu for next batch."
    "ℹ️ Thanks 😍 for using this bot❗️❣️"
    )  
    await message.reply_text(DEFAULT_START_TEXT,reply_markup=B, parse_mode="md") 

    
