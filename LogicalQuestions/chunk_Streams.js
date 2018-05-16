var http = require('http');

var server = http.createServer(function(req, res) {
    let body = "";
    req.setEncoding('utf8');
    req.on('data', (chunk) => {
        console.log('call:', JSON.parse(chunk).call);
        body = chunk;
    });

    req.on('end', () => {
        try {
            const data = JSON.parse(body);
            // write back something interesting to the user:
            res.write(typeof data);
            res.end();
        } catch (er) {
            // uh oh! bad json!
            res.statusCode = 400;
            return res.end(`error: ${er.message}`);
        }
    });

}).listen(3005, function() {
    console.log('running on port: ' + this.address().port);
});;