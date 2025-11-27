"""Example echo server"""

from typing import Any, Callable, Coroutine, Optional, TypeAlias

import websockets

from main import ScreenDisplay

# if you need to define a function with type `ConnectionHandler`, it looks like:
# async def your_function(_: websockets.ServerConnection) -> None
# it will be covered later about `async` and `Coroutine`.
ConnectionHandler: TypeAlias = Callable[
    [websockets.ServerConnection], Coroutine[Any, Any, None]
]


class Server:
    """The server"""

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._screen: Optional[ScreenDisplay] = None

    def bind_screen(self, screen: ScreenDisplay) -> None:
        """Bind the server with screen"""
        if self._screen is None:
            self._screen = screen

    def _handler(self) -> ConnectionHandler:
        if self._screen is None:
            raise RuntimeError("Cannot get handler with screen unbind")

        async def handler(_: websockets.ServerConnection) -> None:
            # in this handler, you may want to define:
            # how to deal with each message (using async with)
            # or you may want to send message, which may take you more than
            # one thread to implement
            raise NotImplementedError

        return handler

    async def serve_forever(self):
        """Serves forever."""
        async with websockets.serve(self._handler(), self._host, self._port) as _:
            # ...serve!
            raise NotImplementedError
