from dotenv import load_dotenv, find_dotenv
from slowapi import Limiter
from slowapi.util import get_remote_address
from os import getenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))

limiter = Limiter(key_func=get_remote_address,
                  default_limits=["3000/day", "5/seconds"],
                  storage_uri=getenv('REDIS_URI'))
