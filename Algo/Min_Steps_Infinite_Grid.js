let A = [4, 8, -7, -5, -13, 9, -7, 8];
let B = [4, -15, -10, -3, -13, 12, 8, -8];

let len = A.length,
    res = 0,
    startA = A[0],
    startB = B[0];

for (i = 1; i < len; i++) {
    let x = Math.abs(startA - A[i]);
    let y = Math.abs(startB - B[i]);
    console.log(x, y);
    startA = A[i];
    startB = B[i];

    res = res + ((x > y) ? x : y);
}

console.log(res);