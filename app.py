import logging
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from slowapi import _rate_limit_exceeded_handler as _rate
from slowapi.middleware import SlowAPIMiddleware
from fastapi_cache import caches
from fastapi_cache.backends.redis import CACHE_KEY
from slowapi.errors import RateLimitExceeded
from config import limiter
from os import getenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))

logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='(%(asctime)s) > %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def _get_database() -> MongoClient:
    """
    Returns the MongoClient Object

            Returns:
                    client (object): MongoClient object
    """

    try:

        client = MongoClient(getenv('MONGO_URI'))

        return client

    except Exception as Error:

        logging.error('Could not establish connection with MongoDB |' + str(Error))


def _create_app() -> FastAPI:
    """
    Create the fastapi application

            Returns:
                    app (object): FastAPI object
    """

    try:

        app = FastAPI(

            title='Lolinck',
            description="Lolinck is an open source API that use machine learning to detect if a website is safe or "
                        "not. It can detect NSFW, phishing, malware, ip logging and more.",
            version='1.0.0',
            docs_url=None

        )

        app.state.limiter = limiter
        app.add_exception_handler(RateLimitExceeded, _rate)
        app.add_middleware(SlowAPIMiddleware)

        return app

    except Exception as Error:

        logging.error('Could not create application |' + str(Error))


def _app_routes(app, routes: list) -> None:
    """
    Include the routes in the application

            Parameters:
                    app (object): FastAPI object
                    routes (list): List of routes

            Returns:
                    None
    """

    try:

        for x in routes:
            app.include_router(x, prefix="/v1")

        return None

    except Exception as Error:

        logging.error('Could not include routes |' + str(Error))


def _redis_cache():
    """
    Caches the Redis instance

        Returns:
            caches (object): Redis Cache Key_func
    """

    return caches.get(CACHE_KEY)
