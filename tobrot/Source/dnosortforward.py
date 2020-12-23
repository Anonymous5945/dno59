import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os
import re
import asyncio
import shlex
from telegraph import Telegraph
from tobrot import (
    DOWNLOAD_LOCATION,
    MAX_MESSAGE_LENGTH,
    chan_ids1,
    chan_ids2
)

import time
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

async def dnosortfor1_f(client, message):
    status_message = await message.reply_text("Processing ...")
    m1 = f"<br><br><br>To See Subtitles Use:<br><br>[android] <a href='https://t.me/xplayerpro'>Xplayer</a> , <a href='https://play.google.com/store/apps/details?id=org.videolan.vlc'>VLC</a> , <a href='https://play.google.com/store/apps/details?id=com.mxtech.videoplayer.ad'>Mxplayer</a><br>[ios] <a href='https://apps.apple.com/us/app/infuse-6/id1136220934'>Infuse</a> , <a href='https://apps.apple.com/us/app/nplayer/id1116905928'>nPlayer</a> , <a href='https://apps.apple.com/us/app/nplayer-lite/id1078835991'>nPlayer Lite</a><br>[PC] <a href='https://potplayer.daum.net/'>Potplayer</a> , <a href='http://en.kmplayer.com/'>Kmplayer</a> , <a href='https://www.videolan.org/index.html'>VLC</a><br><br>If Audio Not working Use VLC [for Android] ,  nPlayer [For ios]<br><br>If video getting struck in mxplayer change decode to sw"
    m3 = f"<a href='http://t.me/kdramaupdates'>Ongoing</a> | <a href='http://t.me/dramaindexchannel'>Index</a> | <a href='http://t.me/Korean_dramas_world'>Completed</a> | <a href='http://t.me/TeamDnO'>D&O</a>"
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    a=[]
    b=[]
    c=[]
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
         j = m.document.file_name
         k = m.document.file_name.lower()
         h = m.document.file_id
         a.append(k)
         b.append(h)
         c.append(j)
     h = [(a[i], b[i], c[i]) for i in range(0, len(a))]
     n = len(h) 
     for i in range(n): 
        for j in range(n-i-1):
            if h[j][0] > h[j + 1][0]:
                 h[j], h[j + 1] = h[j + 1], h[j]

     name , doc = zip(*h)
     for i,j in zip(name,doc):
       if i[:9].lower() == "@dramaost":
        
        for ut in chan_ids1:
         await client.send_document(ut,j, caption= i + "\n\n<b>" + m2 + m3 + "</b>")
         await asyncio.sleep(3)
       elif i[:5].lower() == "[d&o]":
        
        for ut in chan_ids1:
         T=i.split(".mkv")[0]
         await client.send_document(ut,j, caption= T + ".Enc'd.&.Upl'd.By.Team.D&O-@dramaOST.mkv" + "\n\n<b>" + m2 + m3 + "</b>")
         await asyncio.sleep(3)
    await status_message.edit("Finish !!!")

async def dnosortfor2_f(client, message):
    status_message = await message.reply_text("Processing ...")
    m1 = f"<br><br><br>To See Subtitles Use:<br><br>[android] <a href='https://t.me/xplayerpro'>Xplayer</a> , <a href='https://play.google.com/store/apps/details?id=org.videolan.vlc'>VLC</a> , <a href='https://play.google.com/store/apps/details?id=com.mxtech.videoplayer.ad'>Mxplayer</a><br>[ios] <a href='https://apps.apple.com/us/app/infuse-6/id1136220934'>Infuse</a> , <a href='https://apps.apple.com/us/app/nplayer/id1116905928'>nPlayer</a> , <a href='https://apps.apple.com/us/app/nplayer-lite/id1078835991'>nPlayer Lite</a><br>[PC] <a href='https://potplayer.daum.net/'>Potplayer</a> , <a href='http://en.kmplayer.com/'>Kmplayer</a> , <a href='https://www.videolan.org/index.html'>VLC</a><br><br>If Audio Not working Use VLC [for Android] ,  nPlayer [For ios]<br><br>If video getting struck in mxplayer change decode to sw"
    m3 = f"<a href='http://t.me/kdramaupdates'>Ongoing</a> | <a href='http://t.me/dramaindexchannel'>Index</a> | <a href='http://t.me/Korean_dramas_world'>Completed</a> | <a href='http://t.me/TeamDnO'>D&O</a>"
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    a=[]
    b=[]
    c=[]
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
         j = m.document.file_name
         k = m.document.file_name.lower()
         h = m.document.file_id
         a.append(k)
         b.append(h)
         c.append(j)
     h = [(a[i], b[i], c[i]) for i in range(0, len(a))]
     n = len(h) 
     for i in range(n): 
        for j in range(n-i-1):
            if h[j][0] > h[j + 1][0]:
                 h[j], h[j + 1] = h[j + 1], h[j]

     name , doc = zip(*h)
     for i,j in zip(name,doc):
       if i[:9].lower() == "@dramaost":
        
        for ut in chan_ids2:
         await client.send_document(ut,j, caption= i + "\n\n<b>" + m2 + m3 +"</b>")
         await asyncio.sleep(3)
       elif i[:5].lower() == "[d&o]":
        
        for ut in chan_ids2:
         T=i.split(".mkv")[0]
         await client.send_document(ut,j, caption= T + ".Enc'd.&.Upl'd.By.Team.D&O-@dramaOST.mkv" + "\n\n<b>" + m2 + m3 + "</b>")
         await asyncio.sleep(3)
    await status_message.edit("Finish !!!")
