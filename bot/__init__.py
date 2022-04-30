
""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from .get_config import get_config

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = "a0ee8fbebe1950b9291c9e22da4a1450"
APP_ID = "3325855"
# get a token from @BotFather
TG_BOT_TOKEN = "5022849616:AAEZooZmxfOM5PdRIBTsCg7wjptCqhvBLKw"
# array to store the channel ID who are authorized to use the bot
AUTH_CHANNEL = "-1001579836800"

# sqlalchemy Database for the bot to operate
DB_URI = "postgres://rhszvzkrfxnyao:a797729e0c88b8727470b6b14112410d3a0269d9634006c68f0c731f1551fd5f@ec2-54-158-247-210.compute-1.amazonaws.com:5432/d21dgohor98379"
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
#
BAN_COMMAND = get_config("BAN_COMMAND", "ban")
#
UN_BAN_COMMAND = get_config("UN_BAN_COMMAND", "unban")
# start command
START_COMMAND = get_config("START_COMMAND", "start")
HELP_COMMAND = get_config("HELP_COMMAND", help)
# broadcast command
BROADCAST_COMMAND = get_config("BROADCAST_COMMAND","broadcast")
HELP_COMMAND = ("help")
MATHS_COMMAND = ("maths")
PHYSICS_COMMAND = ("physics")
CHE_COMMAND = ("chemistry")
# default message in-case of None types
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
)
DEFAULT_HELP_TEXT = (
    "np help for now check next week"
)
# /start message when other users start your bot
START_OTHER_USERS_TEXT = int(get_config(
    "START_OTHER_USERS_TEXT",
    0
))
# check online status of your bot
ONLINE_CHECK_START_TEXT = get_config(
    "ONLINE_CHECK_START_TEXT",
    (
        "i am online <b>master</b>\n\n"
    )
)
# message to indicate,
# if any message was deleted by the user
# so as to prevent replying to that message
DELETED_MESSAGES_NOTIFICATION_TEXT = get_config(
    "DELETED_MESSAGES_NOTIFICATION_TEXT",
    (
        "this message was deleted\n\n"
    )
)
# IDEKWBYRW
DERP_USER_S_TEXT = get_config(
    "DERP_USER_S_TEXT",
    "😐"
)
# message to show when user is banned
IS_BLACK_LIST_ED_MESSAGE_TEXT = get_config(
    "IS_BLACK_LIST_ED_MESSAGE_TEXT",
    (
        "You have been <b>banned</b> forever.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# IDEKWBYRW
REASON_DE_LIMIT_ER = get_config(
    "REASON_DE_LIMIT_ER",
    "\n\n"
)
# message to show when user is unbanned
IS_UN_BANED_MESSAGE_TEXT = get_config(
    "IS_UN_BANED_MESSAGE_TEXT",
    (
        "You have been <b>un-banned</b>.\n\n"
        "<u>Reason</u>: <code>{reason}</code>"
    )
)
# message to show if bot was blocked by user
BOT_WS_BLOCKED_BY_USER = get_config(
    "BOT_WS_BLOCKED_BY_USER",
    "Bot was blocked by the user."
)
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "NoPMsBot.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)
