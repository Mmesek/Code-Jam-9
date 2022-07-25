from functools import partial
from typing import Coroutine


CLIENT_DISPATCH: dict[str, Coroutine] = {}
"""Registry of functions to run by Client"""
SERVER_OPCODES: dict[str, Coroutine] = {}
"""Registry of functions to run by Server"""


def register(f=None, name: str = None, *, collection: dict):
    """Decorator for functions to run in response to received messages"""

    def inner(f):
        collection[name or f.__name__.upper()] = f
        return f

    if f:
        return inner(f)

    return inner


client = partial(register, collection=CLIENT_DISPATCH)
server = partial(register, collection=SERVER_OPCODES)
