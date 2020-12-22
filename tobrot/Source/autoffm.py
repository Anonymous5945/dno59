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
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    url_parts = shlex.split(message.text)
    if len(url_parts) == 1:
       f1= 1
    elif len(url_parts) == 2:
       n1 = url_parts[1]
    else:
       await status_message.edit("out of bound")
       f1 = 4
    if f1 < 3 :
