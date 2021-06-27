from pyrogram import Client, filters
from pyrogram.types import Message

from bot import AUTH_CHANNEL, COMMM_AND_PRE_FIX, MATHS_COMMAND
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.sql.users_sql import get_chats
import re
import urllib
import urllib.parse
import async_lru
import requests
from bs4 import BeautifulSoup

@Bot.on_message(
    filters.command(MATHS_COMMAND, COMMM_AND_PRE_FIX)
    & uszkhvis_chats_ahndler([AUTH_CHANNEL]))


async def grs(client, message):
   
        return
    query = urllib.parse.quote_plus(query)
    number_result = 8
    ua = UserAgent()
    google_url = (
        "https://teletype.in/@Satyendra/Maths"
    )
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result_div = soup.find_all("div", attrs={"class": "ZINbbc"})
    links = []
    titles = []
    descriptions = []
    for r in result_div:
        try:
            link = r.find("a", href=True)
            title = r.find("div", attrs={"class": "vvjwJb"}).get_text()
            description = r.find("div", attrs={"class": "s3v9rd"}).get_text()
            if link != "" and title != "" and description != "":
                links.append(link["href"])
                titles.append(title)
                descriptions.append(description)
