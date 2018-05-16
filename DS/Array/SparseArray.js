//Sparse Arrays

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_data = '';
var input_array_line = '';
var input_currentline = 0;


process.stdin.on('data', function(data) {
    input_data += data;
});

process.on('SIGINT', function() {
    input_array_line = input_data.split('\n');
    main();
    process.exit();
});

function readLine() {
    return input_array_line[input_currentline++];
}

function main() {
    N = parseInt(readLine());
    Nstring = new Array(N);
    for (i = 0; i < N; i++) {
        Nstring[i] = readLine();
    }

    Q = parseInt(readLine());
    for (i = 0; i < Q; i++) {
        var Qsearch = readLine();
        var count = 0;
        for (j = 0; j < N; j++) {
            if (Qsearch === Nstring[j]) {
                count++;
            }
        }
        console.log(count);
    }


}