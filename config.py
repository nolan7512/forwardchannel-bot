import os

class Config(object):
      API_HASH = os.environ.get("API_HASH")
      API_ID = int(os.environ.get("API_ID", 0))
      AS_COPY = True if os.environ.get("AS_COPY", False) == "True" else False
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      CHANNEL = list(x for x in os.environ.get("CHANNEL_ID", "").replace("\n", " ").split(' '))