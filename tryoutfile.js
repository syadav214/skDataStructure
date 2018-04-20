const fs = require("fs");

const cr = require('crypto');
let xd = cr.randomBytes(20).toString('hex');
console.log(xd, xd.length);



function test() {
    var x = 0;
    let u = 1;

    function ab() {
        console.log(x);
        console.log(u);
    }
    ab();
}

test();


fs.readFile('test.js', function(err, data) {
    if (data) {
        console.log(data.toString());
    }
});


console.log(12);