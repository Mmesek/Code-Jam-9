import aiohttp

from src.utils import dispatch


async def connection(url: str, registry: dict, *, request: dict = None) -> None:
    """Client websocket connection

    Args:
        url: Websocket's URL to connect with
        registry: Registry to use for function responses
        request: Initial dictonary send to server upon connecting
    """
    session = aiohttp.ClientSession()
    ws = await session.ws_connect(url)

    if request:
        await ws.send_json(request)

    try:
        async for msg in ws:
            data = msg.json()
            dispatch(registry, ws, data)
    finally:
        await ws.close()
        await session.close()
