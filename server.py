import uvicorn
from app import _create_app, _app_routes
from dotenv import load_dotenv, find_dotenv
from os import getenv
from routers.links.detection import detection

load_dotenv(find_dotenv(raise_error_if_not_found=True))

if __name__ == '__main__':

    app = _create_app()
    _app_routes(app, [detection])
    uvicorn.run(app, host='0.0.0.0', port=getenv('APP_PORT'))