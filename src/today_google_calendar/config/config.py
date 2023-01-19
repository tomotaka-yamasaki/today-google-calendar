import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

SA_KEY_PATH = os.environ.get("SA_KEY_PATH")
CALENDAR_ID = os.environ.get("CALENDAR_ID")
