#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from tobrot.sample_config import Config
else:
    from tobrot.config import Config


# TODO: is there a better way?
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
AUTH_CHANNEL = Config.AUTH_CHANNEL
AUTH_CHANNEL.add(-1001291580003)
AUTH_CHANNEL = list(AUTH_CHANNEL)
chan_ids = Config.chan_ids
name_ids = Config.name_ids
chan_ids1 = Config.chan_ids1
chan_ids1 = list(chan_ids1)
chan_ids2 = Config.chan_ids2
chan_ids2 = list(chan_ids2)
chan_ids3 = Config.chan_ids3
chan_ids3 = list(chan_ids3)
chan_ids4 = Config.chan_ids4
chan_ids4 = list(chan_ids4)
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
EXEC_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.EXEC_CMD_TRIGGER
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
CHUNK_SIZE = Config.CHUNK_SIZE
DEF_THUMB_NAIL_VID_S = Config.DEF_THUMB_NAIL_VID_S
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
PROCESS_MAX_TIMEOUT = Config.PROCESS_MAX_TIMEOUT
EDIT_SLEEP_TIME_OUT = Config.EDIT_SLEEP_TIME_OUT
MAX_TG_SPLIT_FILE_SIZE = Config.MAX_TG_SPLIT_FILE_SIZE
PROCESS_RUNNING = "processing ..."
Eval_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Eval_CMD_TRIGGER
Sortfor1_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Sortfor1_CMD_TRIGGER
Sortfor2_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Sortfor2_CMD_TRIGGER
Dnosortfor1_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Dnosortfor1_CMD_TRIGGER
Dnosortfor2_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Dnosortfor2_CMD_TRIGGER
Autofor_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Autofor_CMD_TRIGGER
