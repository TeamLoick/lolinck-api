from app import _create_app, _app_routes
from routers.links.detection import detection

app = _create_app()
_app_routes(app, [detection])
