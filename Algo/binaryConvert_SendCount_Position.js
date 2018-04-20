let a = 161;

function valToBin(n) {
    return (n >>> 0).toString(2);
}

let count_of_1 = 0,
    result = [];
i = 1;

valToBin(a).split("").forEach(function(element) {
    if (element === "1") {
        count_of_1 += 1;
        result.push(i);
    }
    i++;
}, this);

result.unshift(count_of_1);