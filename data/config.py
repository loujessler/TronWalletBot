import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

API_TOKEN = str(os.environ.get("API_TOKEN"))

ADMINS = [
    6405640
]

ip = str(os.getenv('ip'))
POSTGRES_USER = str(os.getenv('POSTGRES_USER'))
POSTGRES_PASSWORD = str(os.getenv('POSTGRES_PASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{ip}/{DATABASE}'
