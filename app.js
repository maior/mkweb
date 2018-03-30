var spawn = require("child_process").spawn;

express = require('express')
url = require('url')
app = express()

app.get('/', function (req, res) {
    // res.writeHead(200, {'Content-Type': 'text/html'});
    res.header('Content-type','application/json');
    res.header('Charset','utf8');

    var q = url.parse(req.url, true).query;
    var key = q.key;
    var param = q.func;
    var value = q.value;
    var txdata = '';
    console.log("param %j", param)
    var pythonProcess = spawn('python3', ["loadcontract.py", key, param, value]);
    pythonProcess.stdout.on('data', function (data){
        txdata = data.toString('utf8');
        console.log('results: %j', txdata);
        // res.end(txdata);
        res.send(req.query.callback + '('+ JSON.stringify(txdata) + ');');

    });

})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})

