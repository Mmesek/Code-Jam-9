from src.utils import SERVER_OPCODES, dispatch


async def websocket_handler(request):
    """Main loop of aiohttp's WS server"""
    import aiohttp
    from aiohttp import web

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


async def websocket_endpoint(scope, receive, send):
    """Main loop of starlette's WS server"""
    from starlette.websockets import WebSocket

    websocket = WebSocket(scope=scope, receive=receive, send=send)
    await websocket.accept()
    await websocket.send_json({"type": "hello", "data": {"x": 1}})
    async for data in websocket.iter_json():
        dispatch(SERVER_OPCODES, websocket, data)
