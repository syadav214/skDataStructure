/*
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
*/
import java.io.*;
import java.util.*;

class test {
    

    public static void main(String[] args) {        
        int coins[] = { 1,2,5};
        System.out.println(coinChange(coins, 11));
    }

    static int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        if(amount == 0){
            return 0;
        }
        int[] dp = new int[amount+1];
        Arrays.fill(dp,amount+1);
        dp[0]=0;
        
        for(int j=0;j< coins.length;j++){
            System.out.println("==========================");
            System.out.print("coins[j]: ");
            System.out.println(coins[j]);
            
               for(int i=coins[j];i<=amount;i++){
                System.out.print("i: ");
                System.out.println(i);
                System.out.print("dp[i]: ");
                System.out.println(dp[i]);
                System.out.print("1 + dp[i-coins[j]]: ");
                System.out.println(1 + dp[i-coins[j]]);
                dp[i] = Math.min(dp[i], 1 + dp[i-coins[j]]);  
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];        
    }
}

