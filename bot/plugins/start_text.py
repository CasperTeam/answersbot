

from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AUTH_CHANNEL,
    COMMM_AND_PRE_FIX,
    DEFAULT_HELP_TEXT,
    ONLINE_CHECK_START_TEXT,
    START_COMMAND,
    HELP_COMMAND
)
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler


@Bot.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX)
)

async def nimda_start_message(c, m):
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
    "ℹ️ Subscribe @t24jeetalk 😍 for using this bot❗️❣️"
    )
    await m.reply_text(DEFAULT_START_TEXT)

@Bot.on_message(
    filters.command(HELP_COMMAND, COMMM_AND_PRE_FIX) &
    ~uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def num_start_message(client: Bot, message: Message):
    await message.reply_text(
        client.commandi[HELP_COMMAND],
        quote=True
    )


@Bot.on_message(
    filters.command(HELP_COMMAND, COMMM_AND_PRE_FIX) &
    uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def nimda_start_message(_, message: Message):
    await message.reply_text(
        DEFAULT_HELP_TEXT,
        quote=True
    )
