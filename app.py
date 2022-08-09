from logging import basicConfig
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))

basicConfig(
            filename='app.log',
            filemode='w',
            format='(%(asctime)s) > %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def _get_database() -> MongoClient:
    # Get mongodb database
        
    client = MongoClient(getenv('MONGO_URI'))
        
    return client


def _create_app() -> FastAPI:
    # Create the app 
    
    app = FastAPI()
    
    return app


def _app_routes(app, routes: list) -> None:
    # Include all routes from routers
     
    for x in routes:
            app.include_router(x, prefix="/v1")   
        
    return None
