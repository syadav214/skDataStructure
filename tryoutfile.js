var max1 = -2147483648,
    min1 = 2147483648,
    max2 = -2147483648,
    min2 = 2147483648;
console.log(max1, min1);

var A = [-1000000000, -1000000000, -1000000000, -1000000000, -1000000000];

for (i = 0; i < A.length; i++) {
    max1 = Math.max(max1, A[i] + i);
    min1 = Math.min(min1, A[i] + i);
    max2 = Math.max(max2, A[i] - i);
    min2 = Math.min(min2, A[i] - i);
}

console.log(Math.max(max1 - min1, max2 - min2));

return;


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