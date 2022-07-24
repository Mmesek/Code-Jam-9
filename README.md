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
poetry install
```

Run `client`:
```sh
python -m src.client
```

Run `server`:
```sh
python -m src.server
```

## Extending
In order to extend capabilities, simply add new script or module to `modules` or `plugins`. All modules/plugins will be loaded at startup automatically in these locations.

Extend server capability:
```python
from utils import server, Websocket

@server
async def hello(ws: Websocket, data: dict):
    await ws.send_json({"msg": "Hello there!", "type": "hello_response"})
```

Extend client capability:
```python
from utils import client, Websocket

@client
async def hello_response(ws: Websocket, data: dict):
    print(data["msg"])
```

## Development


## Contributing
Install pre-commit:
```sh
pre-commit install
```

## Team Members
- [Mmesek#2901](https://github.com/Mmesek)
- [Ksenofanex#7782](https://github.com/Ksenofanex)
- [Neur0nz#0095](https://github.com/Neur0nz)
- [MilaDog#1234](https://github.com/MilaDog)
- [Dyna-Soar#5783](https://github.com/Dyna-Soar)
