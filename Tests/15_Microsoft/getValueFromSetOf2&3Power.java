/*
A set consists of 2^P and 3^Q.
e.g.
A[0]=1
A[1]=2
A[2]=3
A[3]=4
A[4]=6
A[5]=8
A[6]=9
A[7]=12
*/

import java.util.*;


class Solution {
    public int solution(int N) {
        ArrayList<Double> arr = new ArrayList<>();
        for(int i =0;i<N+1;i++){
            for(int j =0;j<N+1;j++){
             double twoPow = Math.pow(2,i);
             double threePow = Math.pow(3,j);
             arr.add(twoPow*threePow);
            }
        }
        Collections.sort(arr);
        int value  = (int) Math.round(arr.get(N));
        return value;
    }
}