import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    chan_ids = set(x for x in os.environ.get("chan_ids", "").split())
    chan_ids1 = set(int(x) for x in os.environ.get("chan_ids1", "").split())
    chan_ids2 = set(int(x) for x in os.environ.get("chan_ids2", "").split())
    chan_ids3 = set(int(x) for x in os.environ.get("chan_ids3", "").split())
    chan_ids4 = set(int(x) for x in os.environ.get("chan_ids4", "").split())
    name_ids = set(x for x in os.environ.get("name_ids", "").split())
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # EXEC command trigger
    EXEC_CMD_TRIGGER = os.environ.get("EXEC_CMD_TRIGGER", "exec")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 1))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # Eval command
    Eval_CMD_TRIGGER = os.environ.get("Eval_CMD_TRIGGER", "eval")
    Fir_CMD_TRIGGER = os.environ.get("Fir_CMD_TRIGGER", "")
    Sortfor1_CMD_TRIGGER = os.environ.get("Sortfor1_CMD_TRIGGER", "sort1")
    Sortfor2_CMD_TRIGGER = os.environ.get("Sortfor2_CMD_TRIGGER", "sort2")
    Dnosortfor1_CMD_TRIGGER = os.environ.get("Dnosortfor1_CMD_TRIGGER", "ds1")
    Dnosortfor2_CMD_TRIGGER = os.environ.get("Dnosortfor2_CMD_TRIGGER", "ds2")
    Autofor_CMD_TRIGGER = os.environ.get("Autofor_CMD_TRIGGER", "auto")
