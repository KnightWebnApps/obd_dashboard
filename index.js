const app = require("express")();
const http = require("http").createServer(app);
const io = require("socket.io")(http);
const { spawn } = require("child_process");

io.on("connection", (socket) => {

  console.log('A new connection');

  const proc = spawn('python', ['./main.py']);

  
  proc.stdout.on(
    'data',
    (data) => {
      console.log(`Data : ${data}`);
      const json = JSON.parse(data);
      io.emit('obd', json);
    }  
  );

  proc.stderr.on(
    'data',
    (data) => {
      console.error(`Error: ${data}`);
      function ab2str(buf) {
        return String.fromCharCode.apply(null, new Uint16Array(buf));
      }

      let error = ab2str(data);

      io.emit('obd-err', {"error": error});
      // process.exit(1);
    }
  );

  proc.on('exit', (code, signal) => {
    console.log(`Code: ${code}, Signal: ${signal}`);
  });

});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/client/index.html');
});

http.listen(8000, () => console.log('Listening on 8000'));

