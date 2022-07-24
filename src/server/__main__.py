from aiohttp import web

from src.modules import examples  # noqa: F401
from src.server.websocket import websocket_handler


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get("/", websocket_handler)])
    web.run_app(app, port=8000)
