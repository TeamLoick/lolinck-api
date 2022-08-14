from typing import Any
from fastapi import APIRouter, HTTPException
from lib.validator import site_active, domain_valid
from lib.checker import LinkInfo
from exceptions.IncorrectParameter import IncorrectParamsException

detection = APIRouter()


@detection.get("/detection/", status_code=200)
async def detection_get(url: str) -> str | bool | dict[str, Any]:

    if url == '':
        raise IncorrectParamsException(details="You have not entered any value in the URL parameter")

    if domain_valid(url) is False:
        raise IncorrectParamsException(details="The URL is not valid.")

    if not site_active(url):
        raise IncorrectParamsException(details="The URL is invalid or has not been registered.")

    try:

        info = LinkInfo(url).database_search()

        if info:

            return info

        else:

            return 'Not found'

    except:

        raise 'Link type could not be detected. Please try again'

    return {'url': url}
