#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os

from tobrot import (
    DOWNLOAD_LOCATION,
    TG_BOT_TOKEN,
    APP_ID,
    API_HASH,
    AUTH_CHANNEL,
    EXEC_CMD_TRIGGER,
    Eval_CMD_TRIGGER,
    Dnosortfor2_CMD_TRIGGER,
    Dnosortfor1_CMD_TRIGGER,
    Sortfor1_CMD_TRIGGER,
    Sortfor2_CMD_TRIGGER,
    Autofor_CMD_TRIGGER
)

from pyrogram import (
    Client,
    filters
)
from pyrogram.handlers import (
    MessageHandler,
    CallbackQueryHandler
)

from tobrot.Source.Sort_forward import sortfor2_f , sortfor1_f
from tobrot.Source.autoforward import autofor_f
from tobrot.Source.dnosortforward import dnosortfor2_f , dnosortfor1_f

from tobrot.plugins.status_message_fn import (
    exec_message_f,
    eval_message_f
)

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    app = Client(
        ":memory:",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=343,
        workdir=DOWNLOAD_LOCATION
    )
    #
    exec_message_handler = MessageHandler(
        exec_message_f,
        filters=filters.command([EXEC_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(exec_message_handler)
    #
    eval_message_handler = MessageHandler(
        eval_message_f,
        filters=filters.command([Eval_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(eval_message_handler)
    #
    sortfor1_message_handler = MessageHandler(
        sortfor1_f,
        filters=filters.command([Sortfor1_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(sortfor1_message_handler)
    #
    sortfor2_message_handler = MessageHandler(
        sortfor2_f,
        filters=filters.command([Sortfor2_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(sortfor2_message_handler)
    #
    autofor_message_handler = MessageHandler(
        autofor_f,
        filters=filters.command([Autofor_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(autofor_message_handler)
    #
    dnosortfor1_message_handler = MessageHandler(
        dnosortfor1_f,
        filters=filters.command([Dnosortfor1_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(dnosortfor1_message_handler)
    #
    dnosortfor2_message_handler = MessageHandler(
        dnosortfor2_f,
        filters=filters.command([Dnosortfor2_CMD_TRIGGER]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(dnosortfor2_message_handler)
    #
    app.run()
