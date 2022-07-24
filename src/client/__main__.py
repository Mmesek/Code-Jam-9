import asyncio

from src.client.websocket import connection
from src.modules import examples  # noqa: F401
from src.utils.registry import CLIENT_DISPATCH


URL = "http://localhost:8000/"


if __name__ == "__main__":
    asyncio.run(connection(URL, CLIENT_DISPATCH))
