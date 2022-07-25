# Witty Wyvern's Code Jam 9 Project
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub](https://img.shields.io/github/license/Mmesek/Code-Jam-9)](../../LICENSE.md)

![Lines of code](https://img.shields.io/tokei/lines/github/Mmesek/Code-Jam-9?style=plastic)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Mmesek/Code-Jam-9)]()
[![GitHub repo size](https://img.shields.io/github/repo-size/Mmesek/Code-Jam-9)]()

[![GitHub issues](https://img.shields.io/github/issues/Mmesek/Code-Jam-9)](../../issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Mmesek/Code-Jam-9)](../../pulls)
[![GitHub contributors](https://img.shields.io/github/contributors/Mmesek/Code-Jam-9)](../../graphs/contributors)

## Running
Install requirements
```sh
$ python -m pip install -r requirements.txt
```

Run `client`:
```sh
$ python -m src.client
```

Run `server`:
```sh
$ python -m src.server
```

## Payload
Payload send between client and server should follow this style, and at the very least state `type`:
```json
{
    "type": "remote_function_name", // This is dispatched function on remote client/server.
    "data": {
        // Data can be an arbitrary Dictonary interpreted by remote function,
        // however it's recommended to keep it along these fields for consistency
        "title": "Cool Title",
        "value": 0.0,
        "text": "Descriptive!",
        "footer": "Bottom line"
    },
    "id": "#id" //Related ID for sender
}
```

## Extending
In order to extend capabilities, simply add new script or module to `modules` or `plugins`. All modules/plugins will be loaded at startup automatically in these locations.

Extend server capability:
```python
from utils import server, WebSocket

@server
async def hello(ws: WebSocket, data: dict):
    await ws.send_json(
        {
            "type": "hello_response",
            "data": {
                "text": "Hello there!"
            }
        }
    )
```

Extend client capability:
```python
from utils import client, WebSocket

@client
async def hello_response(ws: WebSocket, data: dict):
    print(data["msg"])
```

## Developement

## Contributing

Install dev dependencies via Pip:
```sh
$ python -m pip install -r dev-requirements.txt
```

Or using Poetry:
```sh
$ poetry install
```

Install pre-commit:
```sh
$ pre-commit install
```

## Docker
Using Docker compose:
```sh
$ docker-compose up
```

Build Docker image:
```sh
$ docker build --target base -t App:latest .
```

Run Docker image
```sh
$ docker run -it --rm NAME
```

## Team Members
- [Mmesek#2901](https://github.com/Mmesek)
- [Neur0nz#0095](https://github.com/Neur0nz)
- [MilaDog#1234](https://github.com/MilaDog)
- [Dyna-Soar#5783](https://github.com/Dyna-Soar)
