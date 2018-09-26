var stdin_input = "5\nC\nC\nA\nB\nA";
var x = stdin_input.split('\n');
var y = {};
var s = [];
for (i = 1; i < x.length; i++) {

    if (x[i] in y) {
        y[x[i]] = y[x[i]] + 1;
    } else {
        y[x[i]] = 1;
    }
}


for (i in y) {
    s.push({ key: i, value: y[i] });
    //s.push([i, y[i]]);
}

s.sort(function(a, b) {
    if (a.key < b.key) return -1;
    if (a.key > b.key) return 1;
    return 0;
});

s.sort(function(a, b) {
    if (b.value < a.value) return -1;
    if (b.value > a.value) return 1;
    return 0;
});

for (i in s) {
    console.log(s[i].key);
}

var arr = Object.keys(y).map(function(key) { return obj[key]; });
let min = Math.min(...arr);
let max = Math.max(...arr);