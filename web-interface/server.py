#!/usr/bin/env python3

# Packages
import asyncio
import websockets


async def python_web_interface(websocket, path):


    # on reçois l'input du client client
    i = 0
    while i < 10:
        input_message = await websocket.recv()
        i = i + 1

        # je créé un fichier html
        f = open('helloworld.html','w')

        ##
        # MESSAGES
        ##
        # header du html
        pythonHtmlHeader = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <link rel="stylesheet" href="master.css">
          <title>Document</title>
        </head>
        <body>

          <div class="jumbotron vertical-center ">
            <div class="container">"""

        # body du html
        pythonHtmlBody = input_message

        # footer du html
        pythonHtmlFooter = """
            </div>
          </div>

        </body>
        </html>"""


        # ici je renvoie un message au client pour dire
        # que j'ai bien reçu le message et que tout c'est bien déroulé
        sentMsg = "Envoyé: " + str(i) + " : " + f"{input_message}!"
        await websocket.send(input_message)
        print("Reçu " + str(i) + ": " + f"{input_message}")

        # j'écris mon code html + message dans mon fichier .html
        f.write(pythonHtmlHeader)
        f.write(pythonHtmlBody)
        f.write(pythonHtmlFooter)
        f.close()

# communique avec mon client
start_server = websockets.serve(python_web_interface, 'localhost', 8765)

# while 42
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
