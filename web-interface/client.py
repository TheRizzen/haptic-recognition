#!/usr/bin/env python3

# WS client example

import asyncio
import websockets

async def hello():
    # on se connecte
    async with websockets.connect(
            'ws://localhost:8765') as websocket:

        # input du user rentré à la main
        i = 0
        while i < 10:
            input_message = input("What do you want to type ?\n ")

            # on dit au server ce qu'on lui envoie
            await websocket.send(input_message)
            i = i + 1

            # le server nous répond pour dire que tout s'est bien passé
            receivedMsg = await websocket.recv()
            print("Envoyé " + str(i) + ": " +f"{receivedMsg}\n")

# pour recevoir des input 24/7
#while 42:
asyncio.get_event_loop().run_until_complete(hello())
