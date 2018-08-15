#!/bin/bash shell

osascript -e 'tell app "Terminal"
  do script "cd Documents/GitHub/haptic-recognition/web-interface;python3 server.py"
  do script "cd Documents/GitHub/haptic-recognition/web-interface;python3 client.py"
  do script "cd Documents/GitHub/haptic-recognition/web-interface;open ./helloworld.html"
end tell'
