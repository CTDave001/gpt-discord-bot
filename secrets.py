import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DISCORD_SECRET = os.environ.get("DISCORD_SECRET")
GUILD_ID = os.environ.get("GUILD_ID")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
