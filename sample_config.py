#  !/usr/bin/env python3
#  Author   : Renjith Mangal| shabib-k

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2130767985:AAG9uZyT6d4C94emicOThIYYyJFPxYYTAj0")
    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "3911505"))
    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "8d055b5e3fb8a249f09cb1b5d7ba3040")
    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")
    # List of admin user ids for special functions(
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "@twomax").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
