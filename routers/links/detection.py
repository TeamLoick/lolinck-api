from fastapi import APIRouter, HTTPException
from lib.validator import site_active, domain_valid
from models.log_model import Log
from modules.database_search import search
from models.add_model import Link

detection = APIRouter()

@detection.get("/detection/")
async def detection_get(url: str, real_time: bool | None = False) -> None:
    
    if url == '':
        raise HTTPException(status_code=400, detail='You did not enter the desired url to be classified.')
    
    if domain_valid(url) is False:
        raise HTTPException(status_code=400, detail='Enter a valid url/domain.')
    
    if site_active(url) != True:
        raise HTTPException(status_code=400, detail='This domain is not registered or is invalid.')
    
    return {'url': url, 'real_time': real_time}
