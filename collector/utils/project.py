import os
from dotenv import load_dotenv

from collector.settings import Settings

load_dotenv()

STOCK_NAME = os.environ.get('STOCK_NAME')


def get_project_settings():

    settings = Settings(stock_name=STOCK_NAME)

    return settings
