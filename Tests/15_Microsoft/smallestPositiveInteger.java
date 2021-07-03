/*
given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

*/

import java.util.*;

class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        Set<Integer> set = new HashSet<Integer>();

        for(int i=0;i< A.length;i++){
            set.add(A[i]);
        }

        int smallestInteger = 1;
        for (Integer i : set) {
            if(smallestInteger == i){
                smallestInteger++;
            }
        }
        return smallestInteger;
    }
}
