/*
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
*/

var max1 = -2147483648,
    min1 = 2147483648,
    max2 = -2147483648,
    min2 = 2147483648;
console.log(max1, min1);

var A = [-1000000000, -1000000000, -1000000000, -1000000000, -1000000000];

for (i = 0; i < A.length; i++) {
    max1 = Math.max(max1, A[i] + i);
    min1 = Math.min(min1, A[i] + i);
    max2 = Math.max(max2, A[i] - i);
    min2 = Math.min(min2, A[i] - i);
}

console.log(Math.max(max1 - min1, max2 - min2));