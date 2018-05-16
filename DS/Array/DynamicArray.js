//Dynamic Array

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function(data) {
    input_stdin += data;
});

process.on('SIGINT', function() {
    input_stdin_array = input_stdin.split("\n");
    main();
    process.exit();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

function main() {
    var rawDataArr = readLine().split(' ');
    var N = parseInt(rawDataArr[0]);
    var I = parseInt(rawDataArr[1]);
    var lastAnswer = 0
    var seqList = new Array(N);
    var seq;
    for (i = 0; i < N; i++) {
        var rawInputs = readLine().split(' ');
        var Q = parseInt(rawInputs[0]);
        var x = parseInt(rawInputs[1]);
        var y = parseInt(rawInputs[2]);
        var index = (x ^ lastAnswer) % N;
        console.log(rawInputs);
        seq = new Array(seqList[index]);
        console.log(Q);
        if (Q == 1) {
            seq.push(y);
        } else {
            var size = seq.length;
            lastAnswer = seq[y % size];
            console.log(size, lastAnswer);
        }
    }
}