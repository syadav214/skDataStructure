/*
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
*/

import java.io.*;
import java.util.*;
//1143.LongestCommonSubsequence
class test {

    public static void main(String[] args) {
        String text1 = "abcde", text2 = "ace";
        System.out.println(longestCommonSubsequence(text1, text2));
    }

    static int longestCommonSubsequence(String text1, String text2) {
        char[] t1 = text1.toCharArray();
        char[] t2 = text2.toCharArray();
        int tL1 = text1.length();
        int tL2 = text2.length();
        
        int[][] dp = new int[tL1+1][tL2+1];
        
        for(int i=0;i<=tL1;i++){
            for(int j=0;j<=tL2;j++){
                if(i==0 || j==0){
                        dp[i][j]=0;
                    } else if(t1[i-1]==t2[j-1]){
                        dp[i][j]=dp[i-1][j-1]+1;
                    } else{
                        dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[tL1][tL2];
        
    }

}

