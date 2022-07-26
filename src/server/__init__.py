from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .websocket import websocket_endpoint


templates = Jinja2Templates(directory="frontend/templates/")


async def homepage(request):
    """Responds with index.html based on template"""
    return templates.TemplateResponse("index.html", {"request": request})


app = Starlette(
    routes=[
        Route("/", endpoint=homepage),
        Route("/ws", endpoint=websocket_endpoint),
        Mount("/static", app=StaticFiles(directory="frontend/static"), name="static"),
    ]
)
