
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os

from tobrot import (
    DOWNLOAD_LOCATION,
    MAX_MESSAGE_LENGTH,
    chan_ids,
    name_ids,
    chan_ids1,
    chan_ids2
)

import asyncio
import time
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

async def autofor_f(client, message):
    status_message = await message.reply_text("Processing ...")
    names =["Sweet.Home","Cheat.On.Me.If.You.Can","The.Goddess.Of.Revenge","True.Beauty","Please.Dont.Date.Him","A.Love.So.Beautiful","Royal.Secret.Agent","Run.On","Hush","Awaken","Lovestruck.In.The.City","Live.On","The.Uncanny.Counter","Mr.Queen","Sunbae.Dont.Put.On.That.Lipstick"]
    chan_ids= ["@SweetHomeNetflix","@cheatonmeifyoucan","@the_goddess_of_revenge_drama","@true_beauty_drama","@Pleasedontdatehim","@a_love_so_beautiful_drama","@royalsecretagent","@runonkdrama2020","@hushkdrama","@awakenkdrama","@lovestruck_in_the_city_drama","@LiveOnkdrama2020","@the_uncanny_counter_kdrama","@Mr_Queen_Drama","@SunbaeDontPutOnthatLipstick"]
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    m1 = f"* <a href='https://telegra.ph/External-Players-12-11-4'>How To see Subtitles</a>\n\n"
    m3 = f"<a href='http://t.me/kdramaupdates'>Ongoing</a> | <a href='http://t.me/dramaindexchannel'>Index</a> | <a href='http://t.me/Korean_dramas_world'>Completed</a>"
    for i in range(w, n):
        u_id = int(i)
        m = await client.get_messages(user_id, u_id)
        if m.media and m.document and m.document.file_name.lower().endswith(".mkv"):
         if m.document.file_name[:9].lower() == "@dramaost":
           for l , s in zip(names,chan_ids):
             h=l.lower()
             b=m.document.file_name.lower()
             if re.search(h,b):
              await client.send_document(message.chat.id,m.document.file_id, caption= m.document.file_name + "\n\n<b>Join: " + s + "\n\n" + m1 +"</b>")
              await asyncio.sleep(3)
         elif m.document.file_name[:5].lower() == "[d&o]":
           for l , s in zip(names,chan_ids):
             h=l.lower()
             b=m.document.file_name.lower()
             if re.search(h,b):
              await client.send_document(message.chat.id,m.document.file_id, caption= m.document.file_name + "\n\n<b>Join: " + s + "\n\n" + m1 +"</b>")
              await asyncio.sleep(3)
    await status_message.edit("Finish !!!")
