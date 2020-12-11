
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
    name_ids
)

import asyncio
import time
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

async def autofor_f(client, message):
