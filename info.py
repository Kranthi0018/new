import re
import os
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


SESSION = environ.get('SESSION', 'media_search')
API_ID = int(environ.get('API_ID', '28912277'))
API_HASH = environ.get('API_HASH', '48b246085fdbc13117b011f5aa8f6b2f')
BOT_TOKEN = environ.get('BOT_TOKEN', "6311976603:AAGpNbWzyK4O7wknQaehkVi5QUx_xq1eW2M")

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/c6599de65447ae1bf5e33-33fc4736f3df295b19.jpg')).split() 
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/62efbcc4e7580b76530ba.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/2A9.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION','https://graph.org/file/695991647c791c56cdafb-090da0f57ef4db003d.jpg'))
FSUB_IMG = (environ.get('FSUB_IMG', 'https://i.ibb.co/cShkPjcZ/x.jpg')).split() 

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5226707402').split()] 
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002066898793'))  
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002066898793'))  
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002066898793'))  
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002066898793')) 
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
reqst_channel = environ.get('REQST_CHANNEL_ID', '-100') 
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002558848039') 
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://friend:friend@cluster0.sv03ooz.mongodb.net/?retryWrites=truemongodb&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False) # Type True For Turn On MULTIPLE DB FUNTION 
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+HILFxi-BYx83MmI9')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/MULTIVERSE_OFCL')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/SUPER_STARR_BOT')
UPDATE_CHANNEL_LNK = environ.get('UPDATE_CHANNEL_LNK', 'https://t.me/MULTIVERSE_UPDATES')

AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1002034875385'))
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '-1002034875385'))

IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002066898793'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002066898793'))
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/Howtodownload18/13")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/Howtodownload18/11")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/")

SHORTENER_API = environ.get("SHORTENER_API", "83d3219341d2c8fe0de09c9d0fe3c54749ceec27")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "gplinks.com")

SHORTENER_API2 = environ.get("SHORTENER_API2", "f06ec4caec5912479b26cf25171559b2da64b52f")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "gyanilinks.com")

SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "")

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "12000"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

MOVIE_UPDATE_NOTIFICATION = bool(environ.get("MOVIE_UPDATE_NOTIFICATION", True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8089")
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us MULTIVERSE♥️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '') 
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))  
LINK_MODE = is_enabled((environ.get('LINK_MODE', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PM_SEARCH = bool(environ.get('PM_SEARCH', True)) 
EMOJI_MODE = bool(environ.get('EMOJI_MODE', True)) 
PAID_STREAM = bool(environ.get('PAID_STREAM', False)) 

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
SEASONS = ["s01" , "s02" , "s03" , "s04", "s05" , "s06" , "s07" , "s08" , "s09" , "s10"]

STREAM_MODE = bool(environ.get('STREAM_MODE', True))

NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
FQDN = "206.189.133.223:8089"
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'SilentXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'SilentX'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', False))
if HAS_SSL:
    URL = "https://lucky-kristyn-daemon990-e8305551.koyeb.app/".format(FQDN)
else:
    URL = "https://lucky-kristyn-daemon990-e8305551.koyeb.app/".format(FQDN)


REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

STAR_PREMIUM_PLANS = {
    1: "7day",
    30: "15day",    
    60: "1month", 
    120: "2month",   
}

Bot_cmds = {
    "start": "ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
    "trendlist": "ɢᴇᴛ ᴛᴏᴘ ꜱᴇᴀʀᴄʜ ʟɪꜱᴛ",
    "myplan" : "ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ",
    "plan" :"ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴘʀɪᴄᴇ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "group_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "admin_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "details": "ꜱᴇᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ",
    "reset_group": "ʀᴇꜱᴇᴛ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ", 
    "stats": "ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ.",
    "delete": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ."
}

#Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2
