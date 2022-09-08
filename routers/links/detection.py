from typing import Any
from json import dumps, loads
from fastapi import APIRouter, Request, Depends
from lib.validator import site_active, domain_valid, url_to_domain
from lib.checker import LinkInfo
from exceptions.IncorrectParameter import IncorrectParamsException
from fastapi_cache.backends.redis import RedisCacheBackend
from app import _redis_cache

detection = APIRouter()


# noinspection PyBroadException
@detection.get("/detection", status_code=200)
async def detection_get(url: str, cache: RedisCacheBackend = Depends(_redis_cache)) -> str | bool | dict[str, Any]:

    if url == '':
        raise IncorrectParamsException(details="You have not entered any value in the URL parameter")

    if domain_valid(url) is False:
        raise IncorrectParamsException(details="The URL is not valid.")

    if not site_active(url):
        raise IncorrectParamsException(details="The URL is invalid or has not been registered.")

    try:

        # We convert the information into a json for saving it in the cache
        domain = url_to_domain(url)
        in_cache = await cache.get(domain)
        info = dumps(LinkInfo(url).database_search())
        info_json = loads(info)

        if not in_cache:
            await cache.set(domain, info_json)

        return in_cache or info_json

    except:
        return 'Link type could not be detected. Please try again'
