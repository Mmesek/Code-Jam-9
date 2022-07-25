class WebSocket:
    """Abstract Websocket Interface"""

    async def close(self):
        """Closes WS channel"""
        raise NotImplementedError

    async def receive_json(self) -> dict:
        """Receive JSON from WS channel"""
        raise NotImplementedError

    async def send_json(self, data: dict) -> None:
        """Send JSON to WS channel"""
        raise NotImplementedError
