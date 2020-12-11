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
    sort_id
)

import asyncio
import time
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

async def sortfor_f(client, message):
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    a=[]
    b=[]
    for i in range(w, n):
        u_id = int(i)
        m = await client.get_messages(user_id, u_id)
        if m.media and m.document and m.document.file_name.lower().endswith(".mkv"):
         j = m.document.file_name
         h = m.message_id
         a.append(j)
         b.append(h)
    h = [(a[i], b[i]) for i in range(0, len(a))]
    n = len(h) 
    for i in range(n): 
        for j in range(n-i-1):
             if h[j][0] > h[j + 1][0]:
                 h[j], h[j + 1] = h[j + 1], h[j]
    name , doc = zip(*h)
    for i,j in zip(name,doc):
       for ut in sort_id:
         await client.forward_messages(
      chat_id=ut,
      from_chat_id=message.chat.id,
      message_ids = j,
      as_copy=True)
         await asyncio.sleep(3)
