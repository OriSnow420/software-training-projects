"""Example echo server"""

import asyncio
import websockets


async def socket_handler(websocket: websockets.ServerConnection) -> None:
    """Socket handler for our easy protocol"""
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected gracefully.")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(type(e))
        print(f"An error occurred: {e}")


async def main():
    """Start the server"""
    async with websockets.serve(socket_handler, "localhost", 1145) as server:
        await server.serve_forever()


asyncio.run(main())
