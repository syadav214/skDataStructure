// Left Rotation of array

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

//console.log('Ctrl + C to get the result===>')

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
    d = parseInt(readLine());
    a = readLine().split(' ');
    finalArray = new Array(lenArray);
    for (i = 0; i < a.length; i++) {
        var index = i - d;
        if (index < 0) {
            index = a.length + index;
        }
        finalArray[index] = a[i];
    }
    console.log(finalArra);
}