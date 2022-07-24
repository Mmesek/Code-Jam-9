import asyncio

import aiohttp

from .models import WebSocket


def dispatch(COLLECTION: dict, ws: WebSocket, data: dict):
    """Dispatches payload to registered function"""
    _function = COLLECTION.get(data["type"].upper())
    if _function:
        asyncio.create_task(_function(ws, data["data"]))


async def get_location_info() -> dict:
    """Returns location info of the client."""
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api64.ipify.org") as response:
            # NOTE: Caching User's IP (and fetching it separately) could prove beneficial
            # if we ever decide to use IP for more than one thing
            ip_address = await response.text()
        async with session.get(f"https://ipapi.co/{ip_address}/json/") as location_response:
            r = await location_response.json(encoding="utf-8")
    return r
