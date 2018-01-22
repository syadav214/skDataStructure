//reverse order of array
process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

console.log('Ctrl + C to get the result===>')

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

/////////////// ignore above this line ////////////////////

function main() {
    var n = parseInt(readLine());
    var arr = readLine().split(' ');
    arr = arr.map(Number);
    var printedNumber = '';
    //console.log(arr);

    for (var i = n - 1; i >= 0; i--) {
        printedNumber += arr[i] + ' ';
    }
    console.log(printedNumber);

}