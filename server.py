from uvicorn import run
from dotenv import load_dotenv, find_dotenv
from fastapi.exceptions import RequestValidationError
from fastapi import Request
from typing import TYPE_CHECKING
from fastapi.responses import JSONResponse
from fastapi_cache import caches, close_caches
from fastapi_cache.backends.redis import CACHE_KEY, RedisCacheBackend
from slowapi.errors import RateLimitExceeded
from os import getenv

if TYPE_CHECKING:
    from routers.links.detection import detection
    from app import _create_app, _app_routes
    from exceptions.IncorrectParameter import IncorrectParamsException

load_dotenv(find_dotenv(raise_error_if_not_found=True))

if __name__ == '__main__':

    app = _create_app()
    _app_routes(app, [detection])

    # Exceptions Handling
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": "Missing required parameters in the request.", "errors": exc.errors(),
                     "docs": "https://docs.lolinck.xyz/errors/parameters"},
        )


    @app.exception_handler(IncorrectParamsException)
    async def incorrect_parameters_handler(request: Request, exc: IncorrectParamsException) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"message": "Your parameters are invalid, try again.", "errors": f'{exc.details}',
                     "docs": "https://docs.lolinck.xyz/errors/parameters"},
        )


    @app.exception_handler(RateLimitExceeded)
    def parse_rate_limit_exception(request: Request, exc: RateLimitExceeded) -> JSONResponse:
        return JSONResponse(
            status_code=429,
            content={"message": f"Maximum limit of requests allowed.",
                     "errors": "You have activated our "
                               "ratelimit, wait a few "
                               "seconds and try again.",
                     "docs": "https://docs.lolinck.xyz/errors/ratelimit"},
        )


    @app.exception_handler(404)
    async def custom_404_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content={"message": f"We were unable to validate your request.", "errors": "This route was not found, "
                                                                                       "check our documentation.",
                     "docs": "https://docs.lolinck.xyz/errors/routes"},
        )


    @app.exception_handler(405)
    async def custom_405_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=405,
            content={"message": "We were unable to validate your request", "errors": "The method you are trying to "
                                                                                     "use is not allowed on this "
                                                                                     "route.",
                     "docs": "https://docs.lolinck.xyz/errors/parameters"},
        )

    # Startup and shutdown handlers
    @app.on_event('startup')
    async def on_startup() -> None:
        rc = RedisCacheBackend(getenv('REDIS_URI'))
        caches.set(CACHE_KEY, rc)


    @app.on_event('shutdown')
    async def on_shutdown() -> None:
        await close_caches()


    run(app, host='0.0.0.0', port=int(getenv('APP_PORT')) or 8000, reload=True)
