# Visual Communication with haptic gloves

### Packages you need to install:
- Express: https://expressjs.com/en/starter/installing.html
```sh
$ npm install express --save
```
- Socket.io
```sh
$ npm install --save socket.io
```
- Yarn: https://yarnpkg.com/lang/en/docs/install/#mac-stable
```sh
$ brew install yarn
```

### Other prerequisite:
- Python 3: https://www.python.org/downloads/
```sh
$ sudo apt-get install python3.6
```
- pip v.18
```sh
$ pip install --upgrade pip
```
- install requirements
```sh
$ pip install -r requirements.txt
```
- install our wrapper
```sh
$ pip install sensoglove
```

### Calibrate the Sensogloves
| Steps | Instruction |
| ------ | ------ |
| 1 | plug your bluetooth dongle |
| 2 | connect the glove to the dongle: (SENSO_BLE_SERVER.exe) |
| 3 | start the UI: (SENSO_UI.exe)
| 4 | clic on 'Connect to server' |
| 5 | select your glove in the list |
| 6 | clic on 'Connect to glove' |
| 7 | clic on 'calibrate', follow instructions on the images |
| 8 | test vibration 'Test vibro' to make sure the glove is connect. Futhermore you should see the data refreshing every ~10ms |

### How to start the project:
| 1. Start server |
| ------ |
| start the server (node app.js) and listen on the port 8080 for any data the glove send us |
```sh
$ yarn start 3000
```
| 2. Open Website |
| ------ |
| open the website in your browser |
```sh
$ firefox index.html
```
| 3. Start software |
| ------ |
| start the software in order to receive the signs and dislpay them on the website |
```sh
$ python3 sign_matching.py [server_address] [listener_port] [website_address] [port_on_which_yarn_listen]
```
#### Description:
Here we use a Virtual Machine.
###### Our [server_address] can be found as follow:
open a terminal:
* cmd (windows)
* ipconfig
* this is your IPv4 address

###### Other Arguments:
* The [listener_port] can be found on the SensoUI, by default it is: 53450.
* The [website_address] is usually localhost since you're going to open the website on your computer.
* The [port_on_which_yarn_listen] corresponds to the first command you did above (1.), here 3000.

>Your command should look like this (with your own server_address/ip):
>python3 sign_matching.py 192.168.56.101 53450 localhost 3000

| 4. Start software |
| ------ |
| if you want to calibrate a sign or create a new sign you need to start our sign_recording.py as follow: |
```sh
$ python3 sign_recording.py [server_address] [listener_port] <file_name>.dat
```

>The <file_name>.dat is of your choosing. by default please leave signDataBank.dat as it >is called by our software.
>But you could change the name of the file that is called in sign_matching.py, ligne 18

In the end you should get this command:
```sh
$ python3 sign_recording.py 192.168.56.101 53450 signDataBank.dat
```

>Once the script executed, make your sign then press r to record the position and name it >(follow instructions). Repeat the process as long as you want to insert signs into our >signDataBank.
>When you are done can press q to quit.

>Restart the the software (3.), go on the website and have fun !


License
----

University of Kent
