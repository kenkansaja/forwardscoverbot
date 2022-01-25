from dotenv import load_dotenv
from os import path, getenv


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN", "1234:abcd")
    ADMINS = int(getenv("ADMINS", None))
    DB_PATH = getenv("DB_PATH", None)
    GROUP = getenv("GROUP", "t.me/musikkugroup")
    CHANNEL = getenv("CHANNEL", "t.me/musikkuchannel")
    KODE = getenv("KODE", "https://github.com/kenkansaja/forwardmediabot")
config = Config()

