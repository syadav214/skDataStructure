const fs = require("fs");


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
return;

fs.readFile('test.js', function(err, data) {
    if (data) {
        console.log(data.toString());
    }
});


console.log(12);