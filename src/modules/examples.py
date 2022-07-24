from src.utils.models import WebSocket
from src.utils.registry import client, server


@server
async def default(ws: WebSocket, data: dict):
    """Responds with close type"""
    print(data)
    await ws.send_json({"type": "close", "data": {"y": 5}})  # This is sent to client


@client
async def hello(ws: WebSocket, data: dict):
    """Example function response"""
    print(data)
    await ws.send_json({"type": "default", "data": {"x": 2}})  # This is sent to server


@client
@server
async def close(ws: WebSocket, data: dict):
    """Closes connection"""
    print("Closing, final data:", data)
    await ws.close()
