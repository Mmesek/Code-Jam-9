import asyncio

import aiohttp

from src.utils.models import WebSocket


def dispatch(COLLECTION: dict, ws: WebSocket, data: dict):
    """Dispatches payload to registered function"""
    _function = COLLECTION.get(data["type"].upper())
    if _function:
        asyncio.create_task(_function(ws, data["data"]))


async def get_ip_address() -> str:
    """Returns IP address of the client."""
    IP_URL = "https://api64.ipify.org?format=json"

    async with aiohttp.ClientSession() as session:
        async with session.get(IP_URL) as ip_response:
            ip_response = await ip_response.json(encoding="utf-8")
            return ip_response["ip"]


async def get_location_info() -> dict:
    """Returns location info of the client."""
    IP_ADDRESS = await get_ip_address()
    LOCATION_URL = f"https://ipapi.co/{IP_ADDRESS}/json/"

    async with aiohttp.ClientSession() as session:
        async with session.get(LOCATION_URL) as location_response:
            return await location_response.json(encoding="utf-8")
