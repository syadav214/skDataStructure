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
    var arr = [];
    for (arr_i = 0; arr_i < 6; arr_i++) {
        arr[arr_i] = readLine().split(' ');

        arr[arr_i] = arr[arr_i].map(Number);
    }

    var sum = 0;
    var maxLength = 5;

    for (i = 0; i < 6; i++) {
        for (j = 0; j < 6; j++) {
            var tempSum = 0;

            var nextC2 = j + 1;
            var nextC3 = j + 2;
            var nextR2 = i + 1;
            var nextR3 = i + 2;

            if (nextC2 <= maxLength && nextC3 <= maxLength && nextR2 <= maxLength && nextR3 <= maxLength) {
                tempSum = arr[i][j] + arr[i][nextC2] + arr[i][nextC3] +
                    arr[nextR2][nextC2] +
                    arr[nextR3][j] + arr[nextR3][nextC2] + arr[nextR3][nextC3];


                if (i == 0 && sum == 0) {
                    sum = tempSum;
                } else if (tempSum > sum) {
                    sum = tempSum;
                }
            }

        }
    }

    console.log(sum);
}