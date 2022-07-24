import aiohttp

from ..utils.utils import dispatch


async def connection(url: str, registry: dict):
    """Client websocket connection"""
    session = aiohttp.ClientSession()
    ws = await session.ws_connect(url)

    try:
        async for msg in ws:
            data = msg.json()
            dispatch(registry, ws, data)
    finally:
        await ws.close()
        await session.close()
