#!/usr/bin/env python3
# server

# Packages
import asyncio
import websockets

pythonHtmlHeader = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="master.css">
  <title>Thesis kent</title>
</head>
<body>
  <div class="jumbotron vertical-center ">
    <div class="container" id="time">"""

pythonHtmlFooter = """
    </div>
  </div>
</body>
<script>
  setInterval("my_function();",1000);

    function my_function(){
        window.location = location.href;
    }
</script>
</html>"""

# create and display our outputs in a html page
async def python_web_interface(websocket, path):
    # var i used to ddisplay the number of the msg received in the terminal
    i = 0
    msg = ""
    while i < 10:
        # on reçois l'input du client client
        input_message = await websocket.recv()

        # if input_message == "RIEN" and bool = 0:
        #     espace
        #     bool = 1
        if input_message == "RIEN":
            pass
        else:
            msg = msg + " " + input_message

            # I create an html file
        f = open('helloworld.html','w')
        ##
        #  PAGE HTML
        ##
        # header
        pythonHtmlHeader
        # body - display my outputs here
        pythonHtmlBody = msg

        # footer
        pythonHtmlFooter

        # here i send a message to the client to tell him that everything went well
        sentMsg = "Envoyé: " + str(i) + " : " + f"{input_message}!"
        await websocket.send(input_message)
        print("Received " + str(i) + ": " + f"{msg}")

        # write html code in my html file i created above
        f.write(pythonHtmlHeader)
        f.write(pythonHtmlBody)
        f.write(pythonHtmlFooter)
        f.close()

        # increment the number of the message
        i = i + 1

# communicate with my client - start server
start_server = websockets.serve(python_web_interface, 'localhost', 8765)

# run until task complete and forever...
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
