import asyncio

from ..modules import examples  # noqa: F401
from ..utils.registry import CLIENT_DISPATCH
from .websocket import connection


URL = "http://localhost:8000/"


if __name__ == "__main__":
    asyncio.run(connection(URL, CLIENT_DISPATCH))
