import os

from dotenv import load_dotenv

load_dotenv()

PORT = os.environ.get("PORT")
HOST = os.environ.get("HOST")
DB_NAME = os.environ.get("DB_NAME")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
