import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

API_TOKEN = str(os.environ.get("API_TOKEN"))

ADMINS = [
    6405640
]

ip = str(os.getenv('ip'))
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URL = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
