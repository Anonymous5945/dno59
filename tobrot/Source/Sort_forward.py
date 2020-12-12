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

async def sortfor1_f(client, message):
   status_message = await message.reply_text("Processing ...")
   n=message.message_id
   w=message.reply_to_message.message_id
   user_id = message.chat.id
   user_id = message.chat.id
   a=[]
   b=[]
   o=[]
   p=[]
   h=[]
   k=[]
   url_parts = shlex.split(message.text)
   if len(url_parts) == 1:
       f1= 1
       m2 = "Muxed English Subtitle"
   elif len(url_parts) == 2:
       n1 = url_parts[1]
       telegraph = Telegraph()
       telegraph.create_account(short_name='1337')
       response = telegraph.create_page(
         "Muxed Subtitles",
         html_content="Muxed Subtitles : " + n1
         )
       file_context= 'https://telegra.ph/{}'.format(response['path'])
       m2 =f"Muxed Subtitles : <a href={file_context}>Click Me</a>\n"
       f1 = 2
   else:
       print("out of bound")
       f1 = 4
   if f1 < 3 :
    for i in range(w, n):
        u_id = int(i)
        m = await client.get_messages(user_id, u_id)
        if m.media and m.document and m.document.file_name.lower().endswith(".mp4"):
         j = m.document.file_name
         h = m.document.file_id
         a.append(j)
         b.append(h)
        if m.media and m.document and m.document.file_name.lower().endswith(".mkv"):
         s = m.document.file_name
         r = m.document.file_id
         o.append(s)
         p.append(r)
    if len(a) != 0:
     h = [(a[i], b[i]) for i in range(0, len(a))]
     n = len(h) 
     for i in range(n): 
        for j in range(n-i-1):
             if h[j][0] > h[j + 1][0]:
                h[j], h[j + 1] = h[j + 1], h[j]
    if len(o) != 0:
     k = [(o[i], p[i]) for i in range(0, len(o))]
     n = len(k) 
     for i in range(n): 
         for j in range(n-i-1):
             if k[j][0] > k[j + 1][0]:
                 K[j], k[j + 1] = k[j + 1], k[j]
    h.extend(k)
    if len(h) != 0:
     name , doc = zip(*h)
     for i,j in zip(name,doc):
      if i[:3].lower() == "kdg":
       if i.lower().endswith(".mkv"):
        for ut in chan_ids1:
         await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles\n\n" + m2 +"\nPlay it via external player</b>")
         await asyncio.sleep(3)
       if i.lower().endswith(".mp4"):
        for ut in chan_ids1:
         await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles</b>")
         await asyncio.sleep(3)
   await status_message.edit("Finish !!!")

async def sortfor2_f(client, message):
   status_message = await message.reply_text("Processing ...")
   n=message.message_id
   w=message.reply_to_message.message_id
   user_id = message.chat.id
   user_id = message.chat.id
   a=[]
   b=[]
   o=[]
   p=[]
   h=[]
   k=[]
   url_parts = shlex.split(message.text)
   if len(url_parts) == 1:
       f1= 1
       m2 = "Muxed English Subtitle"
   elif len(url_parts) == 2:
       n1 = url_parts[1]
       telegraph = Telegraph()
       telegraph.create_account(short_name='1337')
       response = telegraph.create_page(
         "Muxed Subtitles",
         html_content="Muxed Subtitles : " + n1
         )
       file_context= 'https://telegra.ph/{}'.format(response['path'])
       m2 =f"Muxed Subtitles : <a href={file_context}>Click Me</a>\n"
       f1 = 2
   else:
       print("out of bound")
       f1 = 4
   if f1 < 3 :
    for i in range(w, n):
        u_id = int(i)
        m = await client.get_messages(user_id, u_id)
        if m.media and m.document and m.document.file_name.lower().endswith(".mp4"):
         j = m.document.file_name
         h = m.document.file_id
         a.append(j)
         b.append(h)
        if m.media and m.document and m.document.file_name.lower().endswith(".mkv"):
         s = m.document.file_name
         r = m.document.file_id
         o.append(s)
         p.append(r)
    if len(a) != 0:
     h = [(a[i], b[i]) for i in range(0, len(a))]
     n = len(h) 
     for i in range(n): 
        for j in range(n-i-1):
             if h[j][0] > h[j + 1][0]:
                h[j], h[j + 1] = h[j + 1], h[j]
    if len(o) != 0:
     k = [(o[i], p[i]) for i in range(0, len(o))]
     n = len(k) 
     for i in range(n): 
         for j in range(n-i-1):
             if k[j][0] > k[j + 1][0]:
                 K[j], k[j + 1] = k[j + 1], k[j]
    h.extend(k)
    if len(h) != 0:
     name , doc = zip(*h)
     for i,j in zip(name,doc):
      if i[:3].lower() == "kdg":
       if i.lower().endswith(".mkv"):
        for ut in chan_ids2:
         await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles\n\n" + m2 + "\nPlay it via external player</b>")
         await asyncio.sleep(3)
       if i.lower().endswith(".mp4"):
        for ut in chan_ids2:
         await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles</b>")
         await asyncio.sleep(3)
   await status_message.edit("Finish !!!")
