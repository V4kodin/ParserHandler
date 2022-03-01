# file: config.py
from os import environ
from dotenv import load_dotenv
from utils import parse_string

# Загрузка значений переменных окружения
load_dotenv()

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
SESSION_STRING = environ.get('SESSION_STRING')
DATABASE_URL = environ.get('DATABASE_URL')

CHANNELS_MAPPING = parse_string(environ.get('CHANNELS_MAPPING', ''))
SOURCE_CHANNELS = list(CHANNELS_MAPPING.keys())