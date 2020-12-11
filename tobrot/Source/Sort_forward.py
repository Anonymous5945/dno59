import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os
import re
from tobrot import (
    DOWNLOAD_LOCATION,
    MAX_MESSAGE_LENGTH,
    sort_id1,
    sort_id2
)

import asyncio
import time
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

async def sortfor1_f(client, message):
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    a=[]
    b=[]
    o=[]
    p=[]
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
    h = [(a[i], b[i]) for i in range(0, len(a))]
    n = len(h) 
    for i in range(n): 
        for j in range(n-i-1):
             if h[j][0] > h[j + 1][0]:
                h[j], h[j + 1] = h[j + 1], h[j]
    k = [(o[i], p[i]) for i in range(0, len(o))]
    n = len(k) 
    for i in range(n): 
         for j in range(n-i-1):
             if k[j][0] > k[j + 1][0]:
                 K[j], k[j + 1] = k[j + 1], k[j]
    h.extend(k)
    name , doc = zip(*h)
    for i,j in zip(name,doc):
     if i.lower().endswith(".mkv"):
      for ut in sort_id1:
       await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles\n\nMuxed English Subtitles\nPlay it via external player</b>")
       await asyncio.sleep(3)
     if i.lower().endswith(".mp4"):
      for ut in sort_id1:
       await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles</b>")
       await asyncio.sleep(3)
async def sortfor2_f(client, message):
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    a=[]
    b=[]
    o=[]
    p=[]
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
    h = [(a[i], b[i]) for i in range(0, len(a))]
    n = len(h) 
    for i in range(n): 
        for j in range(n-i-1):
             if h[j][0] > h[j + 1][0]:
                h[j], h[j + 1] = h[j + 1], h[j]
    k = [(o[i], p[i]) for i in range(0, len(o))]
    n = len(k) 
    for i in range(n): 
         for j in range(n-i-1):
             if k[j][0] > k[j + 1][0]:
                 K[j], k[j + 1] = k[j + 1], k[j]
    h.extend(k)
    name , doc = zip(*h)
    for i,j in zip(name,doc):
     if i.lower().endswith(".mkv"):
      for ut in sort_id2:
       await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles\n\nMuxed English Subtitles\nPlay it via external player</b>")
       await asyncio.sleep(3)
     if i.lower().endswith(".mp4"):
      for ut in sort_id2:
       await client.send_document(ut,j, caption= "<b>" + i + "\n\n@kdg_166  @korea_drama\n@kdg166_ongoing @kdgfiles</b>")
       await asyncio.sleep(3)
