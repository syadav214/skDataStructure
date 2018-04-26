A = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
li = 0;
ri = 0;
maxSum = A[0];
maxSumTillLast_i = A[0]



for (i = 1; i < A.length; i++) {
    var newStart = false;
    var num = A[i];
    maxSumTillLast_i = maxSumTillLast_i + num;

    if (num >= maxSumTillLast_i) {
        maxSumTillLast_i = num;
        newStart = true;
    }

    if (maxSumTillLast_i >= maxSum) {
        maxSum = maxSumTillLast_i;
        if (newStart) {
            li = i;
        }
        ri = i;
    }
}

console.log(maxSum);

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