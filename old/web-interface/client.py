#!/usr/bin/env python3
# client

# Packages
import asyncio
import websockets

from display import *

async def hello():
    # connection
    async with websockets.connect('ws://localhost:8765') as websocket:
        # var i used to ddisplay the number of the msg received in the terminal
        i = 0
        while i < 10:
            # TODO: replace user inputs by gloves output
            sign = displayToClient()
            #input_message =

            # send input to server
            if sign == "NOTHING":
                pass
            else:
                #print(detect_sign(fingers))
                await websocket.send(str(sign))

            # the server tell us everything went well
            receivedMsg = await websocket.recv()
            print("Sent " + str(i) + ": " +f"{receivedMsg}\n")
            # increment the number of the message
            i = i + 1


# run until task complete and forever...
asyncio.get_event_loop().run_until_complete(hello())
