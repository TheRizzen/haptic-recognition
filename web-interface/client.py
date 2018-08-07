#!/usr/bin/env python3
# client

# Packages
import asyncio
import websockets

async def hello():
    # connection
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
        # var i used to ddisplay the number of the msg received in the terminal
        i = 0
        while i < 10:
            # TODO: replace user inputs by gloves output
            input_message = input("What do you want to type ?\n ")

            # send input to server
            await websocket.send(input_message)

            # the server tell us everything went well
            receivedMsg = await websocket.recv()
            print("Envoyé " + str(i) + ": " +f"{receivedMsg}\n")

            # increment the number of the message
            i = i + 1


# run until task complete and forever...
asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
