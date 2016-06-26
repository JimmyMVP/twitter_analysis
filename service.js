//var spawn = require("child_process").spawn;
//var process = spawn('python',["path/to/script.py", arg1, arg2, ...]);

ipc = require("node-ipc")



//while(true) {

    socket = ipc.connectTo("pysocket", "pysocket" , function() {

        ipc.of.pysocket.on("connect", function() {

            console.log("Connected")

        })


        ipc.of.pysocket.on("data", function(data) {


            console.log(data)


        })
    });

//