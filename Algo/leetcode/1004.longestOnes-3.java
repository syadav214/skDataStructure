/*
Max Consecutive Ones III
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

*/

class Solution {
    public int longestOnes(int[] nums, int k) {
        int ans = 0, l = 0;
        
        for(int r = 0; r < nums.length;r++){
            if(nums[r] == 0){
                if(k == 0){
                    while(nums[l++] != 0);
                } else {
                    k--;    
                }
                
            }
            ans = Math.max(ans, r - l + 1);
        }
        return ans;
        
    }
}