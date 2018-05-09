/*
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
*/
var hasExtra = true;

for (var i = A.length - 1; i >= 0; i--) {
    if (!hasExtra)
        break;

    A[i] = (A[i] + 1) % 10;
    hasExtra = false;

    if (A[i] == 0) {
        hasExtra = true;
    }
}

if (hasExtra) {
    A.unshift(1);
}

while (A[0] == 0) {
    A.shift();
}

return A;