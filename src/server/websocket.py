import aiohttp
from aiohttp import web

from src.utils import SERVER_OPCODES, dispatch


async def websocket_handler(request: web.Request):
    """Main loop of aiohttp's WS server"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print("New ws connection")
    await ws.send_json({"type": "hello", "data": {"x": 1}})  # Initial payload, to start things up

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            data = msg.json()
            dispatch(SERVER_OPCODES, ws, data)

        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f"ws connection closed with exception {ws.exception()}")

    print("websocket connection closed")

    return ws
