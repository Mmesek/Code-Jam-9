import asyncio

from .models import WebSocket


def dispatch(COLLECTION: dict, ws: WebSocket, data: dict):
    """Dispatches payload to registered function"""
    _function = COLLECTION.get(data["type"].upper())
    if _function:
        asyncio.create_task(_function(ws, data["data"]))
