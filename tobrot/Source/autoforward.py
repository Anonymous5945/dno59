
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os
import re
from telegraph import Telegraph
import shlex
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
    m1 = f"<br><br><br>To See Subtitles Use:<br><br>[android] <a href='https://t.me/xplayerpro'>Xplayer</a> , <a href='https://play.google.com/store/apps/details?id=org.videolan.vlc'>VLC</a> , <a href='https://play.google.com/store/apps/details?id=com.mxtech.videoplayer.ad'>Mxplayer</a><br>[ios] <a href='https://apps.apple.com/us/app/infuse-6/id1136220934'>Infuse</a> , <a href='https://apps.apple.com/us/app/nplayer/id1116905928'>nPlayer</a> , <a href='https://apps.apple.com/us/app/nplayer-lite/id1078835991'>nPlayer Lite</a><br>[PC] <a href='https://potplayer.daum.net/'>Potplayer</a> , <a href='http://en.kmplayer.com/'>Kmplayer</a> , <a href='https://www.videolan.org/index.html'>VLC</a><br><br>If Audio Not working Use VLC [for Android] ,  nPlayer [For ios]<br><br>If video getting struck in mxplayer change decode to sw"
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id 
    m3 = f"<a href='http://t.me/kdramaupdates'>Ongoing</a> | <a href='http://t.me/dramaindexchannel'>Index</a> | <a href='http://t.me/Korean_dramas_world'>Completed</a> | <a href='http://t.me/TeamDnO'>D&O</a>"
    url_parts = shlex.split(message.text)
    if len(url_parts) == 1:
       f1= 1
       telegraph = Telegraph()
       telegraph.create_account(short_name='1337')
       response = telegraph.create_page(
         "Muxed English Subtitles",
         html_content= m1
         )
       file_context= 'https://telegra.ph/{}'.format(response['path'])
       m2 = f"<a href={file_context}>🍁 Muxed English Subtitle 🍁</a>\n\n"

    elif len(url_parts) == 2:
       n1 = url_parts[1]
       telegraph = Telegraph()
       telegraph.create_account(short_name='1337')
       response = telegraph.create_page(
         "Muxed Subtitles",
         html_content="Muxed Subtitles : " + n1 + m1
         )
       file_context= 'https://telegra.ph/{}'.format(response['path'])
       m2 =f"<a href={file_context}>🍁 Muxed Multi Subtitles 🍁</a>\n\n"
       f1 = 2
    else:
       await status_message.edit("out of bound")
       f1 = 4
    if f1 < 3 :
     for i in range(w, n):
        u_id = int(i)
        m = await client.get_messages(user_id, u_id)
        if m.media and m.document and m.document.file_name.lower().endswith(".mkv"):
         if m.document.file_name[:9].lower() == "@dramaost":
           for l , s in zip(name_ids,chan_ids):
             h=l.lower()
             b=m.document.file_name.lower()
             if re.search(h,b):
              for ut in chan_ids1:
               await client.send_document(ut,m.document.file_id, caption= m.document.file_name + "\n\n<b>Join: " + s + "\n\n" + m2 + m3 +"</b>")
               await asyncio.sleep(3)
         elif m.document.file_name[:5].lower() == "[d&o]":
           for l , s in zip(name_ids,chan_ids):
             h=l.lower()
             b=m.document.file_name.lower()
             if re.search(h,b):
              for ut in chan_ids1:
               T= m.document.file_name.split(".mkv")[0]
               await client.send_document(ut,m.document.file_id, caption= T + ".Enc'd.&.Upl'd.By.Team.D&O-@dramaOST.mkv" + "\n\n<b>Join: " + s + "\n\n" + m2 + m3 +"</b>")
               await asyncio.sleep(3)
    await status_message.edit("Finish !!!")
