# Client/Server
Client/Server behaviour & coding functionalities.

## Installation
### Install dependencies
```sh
python -m pip install -r requirements.txt
```

## Running
### Server
Run `server`:
```sh
python -m src.server
```

### Client
Once you get server running, run `client`:
```sh
python -m src.client
```

## Function Registry

`registry.py` is a file containing decorator for registering functions to be executed by server/client upon receiving data with name of function in `type`.

## Payload & Client/Server Functions
Example Payload:
```json
{
    "type": "hello",
    "data": {
        "x": 1
    }
}
```
This payload is sent by server upon new client's connection, in which case `client.py` executes example `hello` function located in `examples.py`.

Currently the only parameters supported are `websocket` and `data`, though some sort of cache functionality to maintain data between websocket payloads might be worth addition
