var PythonShell = require('python-shell');

var options = {
    mode: 'json',
    pythonOptions: ['-u'],
    scriptPath: './',
	//args: "COM"
};

var Monitor =  new PythonShell('nodeCommandAPI.py', options);
Monitor.on('message',function (message) {
    console.log(message);
});