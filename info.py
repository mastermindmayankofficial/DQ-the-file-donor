import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/923a13614827ccf1a2e90.mp4 https://telegra.ph/file/6c5bc55b73384ba4c303a.mp4 https://telegra.ph/file/d91ac1f53b5125854bf71.mp4 https://telegra.ph/file/1d590e56cf43d28410a88.mp4 https://telegra.ph/file/20d9d8781af327d92b0da.mp4 https://telegra.ph/file/3f4a3325a2e9b398f9046.mp4 https://telegra.ph/file/90160266b49ece48609ab.mp4 https://telegra.ph/file/3746cf10991d16a6430cc.mp4 https://telegra.ph/file/831e99f7befb90f9be7f4.mp4 https://telegra.ph/file/ab2c0589c04f5b289b74e.mp4 https://telegra.ph/file/7de252ef62a8660f87dce.mp4 https://telegra.ph/file/2280a2fa537b75ca1f1ac.mp4')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/f91cefd6b2d084e743bb2.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/5fb1cf8ba009fd80ca679.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/b66f3a65ce68e11e621cf.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5925346074 5864126910').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL',"-1001559607832")
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "mastermind")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
STICKER = (environ.get('STICKER', 'CAACAgUAAxkBAAIEVWL6C28YSH-wls4oFFrziOCoUMUqAALDBQACbBS5V2NazuHcCfEPHgQ CAACAgUAAxkBAAIEVGL6C2lelc69C6FICGN9bwhWKY4GAAKwBgACxS6wVwr0-R_TTet3HgQ CAACAgUAAxkBAAIEQWL6C0-i60ZXLmNfrfGyF-tXQ8mGAAJ2BgACFPGhV5YGbchd7kR-HgQ CAACAgUAAxkBAAIEQmL6C0nFxWYjAzJkfqkdA34HARbJAAIPCAACuc2pV35uuVLrsyJzHgQ CAACAgUAAxkBAAIEQ2L6C0TYb7bWLdthTyt0J-YKL5b8AAKMBwACopOpV8IkcbZ5awoPHgQ CAACAgUAAxkBAAIERWL6Czw2n7TBN5akcqeSKEeevzAgAAJIBQACa-G5VwNKMtODitd-HgQ CAACAgUAAxkBAAIEQ2L6C0TYb7bWLdthTyt0J-YKL5b8AAKMBwACopOpV8IkcbZ5awoPHgQ CAACAgUAAxkBAAIERGL6CzGXttOUvN_ThfEDg50zHdqrAAI3BwACEeChV2V-xjqOmtXcHgQ CAACAgUAAxkBAAIER2L6CytH_f5s7-HaiBj6jx-TRdLZAAJYBgACDoyxVwRYoe_-SpZQHgQ CAACAgUAAxkBAAIEPmL6CwZED9KoGu2l1fHWtU9Bv9HgAAKVBQACuo6gV4yViYWXvwpDHgQ CAACAgUAAxkBAAIEO2L6CvdzL2WiTPrRQMRPIBdy11XYAAKuBgACv9ygV_m09JLhcXVnHgQ')).split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/mastermindmayankmoviez')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/mastermindmayankproject')
MSG_ALRT = environ.get('MSG_ALRT', 'Thanks to Mastermind Mayank')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001675952180'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'mastermindmayankmoviez')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001675952180')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
