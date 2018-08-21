# Visual Communication with haptic gloves


## Installation

### Sign Recognition

Move to sign recognition folder

```sh
$ cd Source_Code/version_1.0_CORPUS/sign_recognition
```

Install the dependencies

```sh
$ pip -r requirements.txt
```

### Web Interface

Move to web interface forlder

```sh
$ cd Source_Code/version_1.0_CORPUS/web_interface
```

Install the dependencies

```sh
$ npm install
```

## Install and calibrate the Sensogloves

https://senso.me/dev

| Steps | Instruction |
| ------ | ------ |
| 1 | plug your bluetooth dongle |
| 2 | connect the glove to the dongle: (SENSO_BLE_SERVER.exe) |
| 3 | start the UI: (SENSO_UI.exe)
| 4 | click on 'Connect to server' |
| 5 | select your glove in the list |
| 6 | click on 'Connect to glove' |
| 7 | click on 'calibrate', follow instructions on the images |
| 8 | test vibration 'Test vibro' to make sure the glove is connect. Futhermore you should see the data refreshing every ~10ms |

## How to start the project
### 1. Start web interface
Start the web interface and listen on the port 8080 for any data the glove send us
```sh
$ yarn start 3000
```

### 2. Open Website
Open the web page in your browser
```sh
$ firefox localhost:8080
```

### 3. Start the Sign Recognition script
Start the script in order to receive the signs and send them to the web interface
```sh
$ python3 sign_matching.py <glove_host> <glove_port> <webinterface_host> <webinterface_listing_port> <signsbank_file.dat>
```

#### Description:

###### Arguments:
* `glove_host` and <glove_port> can be found on the SensoUI.
* `webinterface_host` is usually localhost since you're going to open the website on your computer.
* `webinteface_listening_port` corresponds to the first command you did above (1.), here 3000.

>Your command should look like this (with your own server_address/ip):
>python3 sign_matching.py 192.168.56.101 53450 localhost 3000

## Record new signs
If you want to create a new sign you need to start sign_recording.py as follow:
```sh
$ python3 sign_recording.py <glove_host> <glove_port> <file_name.dat>
```

>The <file_name.dat> is of your choosing. By default you can use signDataBank.dat

In the end you should get this command:
```sh
$ python3 sign_recording.py 192.168.56.101 53450 signDataBank.dat
```

>Once the script executed, make your sign then press r to record the position and name it (follow instructions). Repeat the process as long as you want to insert signs into your signDataBank.
>When you are done can press q to quit.

>Restart the the software (3.), go on the website and have fun !

# Requirements
- [Express](https://expressjs.com/en/starter/installing.html)
- [Socket.io](https://socket.io/)
- [Python3.x](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Npm](https://www.npmjs.com/)
- Senso-Driver v08.06.2018


# License

MIT

Copyright (c) 2018 Anthony ABRAMO, Hugo DARSES, Thibault Miranda de Oliveira
