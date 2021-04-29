/*
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

*/

import java.io.*;
import java.util.*;

class test {

    public static void main(String[] args) {
        int[] arr = {3,1,5,8};
        System.out.println(burstBallon(arr));
    }

    static int burstBallon(int[] arr){
        int s = arr.length;
        int[][] dp = new int[s][s];
        for(int L=s-1;L>-1;L--){
            for(int R=L;R<s;R++){
                for(int i=L;i<=R;i++){
                    dp[L][R] = Math.max(dp[L][R],
                            arr[i]* (L-1 < 0 ? 1: arr[L-1])*(R+1 > s-1 ? 1 : arr[R+1])
                            + (L <=i-1 ? dp[L][i-1] : 0)
                            +(i+1 <= R ? dp[i+1][R]:0)
                            );
                }
            }
        }
        return dp[0][s-1];
    }

}

