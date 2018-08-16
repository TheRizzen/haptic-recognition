# haptic-recognition

###############
Packages you need to install:

https://expressjs.com/en/starter/installing.html
npm install express --save

https://socket.io/get-started/chat/
npm install --save socket.io

https://yarnpkg.com/lang/en/docs/install/#mac-stable
brew install yarn (macOS)



###############
Other prerequisite:

you need python3:
https://www.python.org/downloads/
sudo apt-get install python3.6

update pip to v.18:
pip install --upgrade pip

install requirements:
pip install -r requirements.txt

install our wrapper
pip install sensoglove



###############
Calibrate the Sensogloves (folder 'senso-driver-latest'):

1. plug your bluetooth dongle

2. connect the glove to the dongle:
 start 'SENSO_BLE_SERVER.exe'

3. start the UI:
start 'SNESO_UI.exe'

4. clic on 'Connect to server'

5. select your glove in the list

6. clic on 'Connect to glove'

7. clic on 'calibrate', follow instructions on the images

8. test vibration 'Test vibro' to make sure the glove is connect. Futhermore you should see the data refreshing every ~10ms



###############
How to start the project:

1. start the server (node app.js) and listen on the port 8080 for any data the glove send us
yarn start 3000


2. open the file index.html in your browser


3. start the software in order to receive the signs and dislpay them on the website:

python3 sign_matching.py [server_address] [listener_port] [website_address] [port_on_which_yarn_listen]

Description:
Here we use a Virtual Machine.
- Our [server_address] can be found as follow:
open a terminal:
  - cmd (windows)
  - ipconfig
  - this is your IPv4 address

- The [listener_port] can be found on the SensoUI, by default it is: 53450.

- The [website_address] is usually localhost since you're going to open the website on your computer.

- The [port_on_which_yarn_listen] corresponds to the first command you did above (1.), here 3000.

Your command should look like this (with your own server_address/ip):
python3 sign_matching.py 192.168.56.101 53450 localhost 3000


4. if you want to calibrate a sign or create a new sign you need to start our sign_recording.py as follow:

python3 sign_recording.py [server_address] [listener_port] <file_name>.dat

The <file_name>.dat is of your choosing. by default please leave signDataBank.dat as it is called by our software.
But you could change the name of the file that is called in sign_matching.py, ligne 18

In the end you should get this command:
python3 sign_recording.py 192.168.56.101 53450 signDataBank.dat

Once the script executed, make your sign then press r to record the position and name it (follow instructions). Repeat the process as long as you want to insert signs into our signDataBank.
When you are done can press q to quit.

Restart the the software (3.), go on the website and have fun !
