function findDigits(n) {
    let count = 0;
    n.toString().split('').forEach(num => {
        if (num != '0' && n % parseInt(num) == 0) {
            count++;
        }
    });
    return count;
}

console.log(findDigits(1012));