/*
You are given 30-bit unsigned integer N. A right cyclic shift of N by K bits is the result of performing a right cyclic shift of N by one bit K times. Leading zeros may appear.

For example:
the right cyclic shift of 9736 by one bit is 4868,
the right cyclic shift of 9736 by two bits is 2434,
the right cyclic shift of 9736 by eleven bits is 809500676

The number 809500676 is the largest value that can be obtained by performing a right cyclic shift of 9736.

The aim is to find integer K such that right cyclic shift of N by K bits gives the largest possible value. In example above method should return 11. 0<=N<=1073741823. Worst-case time complexity is O(log(N)).

*/

class Solution {
    int solution(int N) {
        int largest = 0;
        int shift = 0;
        int temp = N;
        for (int i = 1; i < 30; ++i) {
            int index = (temp & 1);
            temp = ((temp >> 1) | (index << 29));
            if (temp > largest) {
                largest = temp;
                shift = i;
            }
        }
        return shift;
    }
}
