#!/usr/bin/env python3

# WS client example

import asyncio
import websockets

async def hello():
    async with websockets.connect(
            'ws://localhost:8765') as websocket:

        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

while 42:
    asyncio.get_event_loop().run_until_complete(hello())
