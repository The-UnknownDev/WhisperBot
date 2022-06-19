import os

#BURI NAJAR WALE TERA MUH GAAND JAISA
# Config Vars
BYTEAPI_HASH = "4af0dda44fd0209249bb9a482690506c"
BYTEAPI_KEY = 9197144
BYTEBOT_NAME = os.environ.get("BOT_NAME", None) # Your bot name, example: Null Bot
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) # Your bot username with (@), example: @WhisperNRobot
BYTE_TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather

# Config Text
START_TEXT = f"**Heya,there I am a {BYTEBOT_NAME}!**\n\nType /help to see how to use me!\ {BYTEBOT_NAME}.\n Powered by [The Byte Bots](https://t.me/TheByteBots)"

HELP_TEXT = f"**• How to use {BYTEBOT_NAME}:**\n\nClick the button below or\n\nType __{BOT_USERNAME} wspr <username> | <text>__\nExample: `{BOT_USERNAME} wspr @Arpit_Chaurasiya | Hello!`\nHow are you sir"

REPO_TEXT = f"Click the button below to deploy bot like {BYTEBOT_NAME} Thankyou"
