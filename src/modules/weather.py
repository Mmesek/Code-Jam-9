import aiohttp

from src.utils import dispatch
from src.utils.models import WebSocket
from src.utils.registry import client, server


def do_this_too():
    return "Yebo mate"


@client
async def get_weather_data():
    url = "http://localhost:8000/"
    session = aiohttp.ClientSession()
    ws = await session.ws_connect(url)

    registry = {"type": "request_weather_data"}

    # if request:
    #     await ws.send_json(request)

    try:
        async for msg in ws:
            data = msg.json()
            dispatch(registry, ws, data)
    finally:
        await ws.close()
        await session.close()

    print(ws)


@client
async def request_weather_data(ws: WebSocket):
    """Sends request to server for weather data to display"""
    await ws.send_json({"type": "send_weather_data"})  # send to server


@server
async def send_weather_data(ws: WebSocket):
    """Returns the fetched weather data to the user"""
    _weather_data = {
        "type": "xx",
        "data": {"title": "Celsius", "value": 10.3, "description": "Windy", "footer": "It's a bit chilly out there!"},
    }
    await ws.send_json(_weather_data)  # send to client


@client
async def display_weather_data(ws: WebSocket, data: dict):
    print(data)


if __name__ == "__main__":
    print("herhe")
    # get_weather_data()
