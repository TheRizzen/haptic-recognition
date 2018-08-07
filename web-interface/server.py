#!/usr/bin/env python3

# Packages
import asyncio
import websockets


async def python_web_interface(websocket, path):

    # on reçois l'input du client client
    message = await websocket.recv()

    # j'affiche l'input dans côté client (terminal)
    # pour debug - peut être retiré
    print(f"< {message}")
    greeting = f"Hello {message}!"

    # je créé un fichier html
    f = open('helloworld.html','w')

    # message qu'on passe au fichier .html
    # contient tout le html et concatène avec
    # l'input pour l'afficher dans le html
    pythonHtml = """
    <html>
    <head></head>
    <body>
        <p>hello</p>"""+\
        message +\
    """
    </body>
    </html>"""

    # ici je renvoie un message au client pour dire
    # que j'ai bien reçu le message et que tout c'est bien déroulé
    await websocket.send(greeting)
    print(f"> {greeting}")

    # j'écris mon code html + message dans mon fichier .html
    f.write(pythonHtml)
    f.close()

# communique avec mon client
start_server = websockets.serve(python_web_interface, 'localhost', 8765)

# while 42
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
