import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'new.env')
load_dotenv(dotenv_path)

#DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
DISCORD_SECRET = os.environ.get("DISCORD_SECRET")
GUILD_ID = os.environ.get("GUILD_ID")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
the_id_of_your_guild = 1100154123116101673

