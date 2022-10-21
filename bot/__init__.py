# Powred By Bikash Gadgets Tech 
# Owner Of Bgt BikashHalder
# Bikash Bro Aditya Halder

import asyncio

from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.API_ID,api_hash=Config.API_HASH,bot_token=Config.BOT_TOKEN)


SUDO = Config.SUDO
OWNER = config.OWNER







@bot.on_message(filters.command("banall") & filters.group)
def NewChat(bot,message):
    logging.info("🌷 𝐍𝐞𝐰 𝐂𝐡𝐚𝐭 {}".format(message.chat.id))
    logging.info("🌷 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐅𝐨𝐫𝐦 {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("📌 𝐊𝐢𝐜𝐤𝐞𝐝 {} 𝐅𝐫𝐨𝐦 {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" ❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐊𝐢𝐜𝐤 {} 𝐅𝐫𝐨𝐦 {}".format(i.user.id,message.chat.id))
            
    logging.info("📌 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝 ✅")



@bot.on_message(filters.command("start") & filters.private)
async def hello(bot, message):
    await message.reply("🌷 𝐇𝐞𝐲, 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐁𝐚𝐧𝐚𝐥𝐥 𝐁𝐨𝐭 💖 𝐈 𝐂𝐚𝐧 𝐁𝐚𝐧 𝐀𝐧𝐲 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐖𝐢𝐭𝐡𝐢𝐧 𝐅𝐞𝐰 𝐌𝐨𝐦𝐦𝐞𝐧𝐭 ✅\n\n 🌸 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐌𝐞 𝐚 𝐀𝐝𝐦𝐢𝐧 𝐖𝐢𝐭𝐡 𝐁𝐚𝐧 𝐑𝐢𝐠𝐡𝐭 🌷 𝐓𝐡𝐞𝐧 𝐓𝐲𝐩𝐞 𝐀𝐧𝐲 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 𝐖𝐡𝐨 𝐎𝐧𝐞 𝐁𝐚𝐧 𝐓𝐡𝐞 𝐆𝐫𝐨𝐮𝐩 ✅ ({OWNER}) ")

