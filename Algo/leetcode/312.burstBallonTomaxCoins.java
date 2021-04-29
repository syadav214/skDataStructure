
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

