const net = require('net');
const path = require('path');
const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

const port = process.env.API_PORT || 8080;

const signsPort = process.argv[2] || 3000

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

net.createServer((socket) => {
  socket.on('data', (data) => {
    sign = JSON.parse(data)
    console.log(sign);
    io.emit('new_sign', sign.meaning);
  })
}).listen(signsPort);

http.listen(port, () => console.log(`listening on ${port}`));
