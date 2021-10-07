var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');
var serverUptime = os.uptime();
let serverSeconds = (serverUptime / 1000);
let sdays = Math.floor(serverSeconds / 86400);
let shours = Math.floor(serverSeconds / 3600);
serverSeconds %= 3600; 
let sminutes = Math.floor(serverSeconds / 60);
let sseconds = Math.floor(serverSeconds % 60);
var serverUptimeCalc = `${sdays} days, ${shours} hours, ${sminutes} minutes and ${sseconds} seconds`;


var server = http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        myCPU=os.cpus().length;

        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${serverUptimeCalc} </p>
            <p>Total Memory: ${os.totalmem() / 1024 / 1024 + "MB" } </p>
            <p>Free Memory: ${os.freemem() /1024 / 1024 + "MB"} </p>
            <p>Number of CPUs: ${myCPU} </p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
