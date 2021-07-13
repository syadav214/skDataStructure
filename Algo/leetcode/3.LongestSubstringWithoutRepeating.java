/*
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int size = 0, left = 0;
        Set<Character> seen = new HashSet<>();
        for(int j=0;j<s.length();j++){
            while(seen.contains(s.charAt(j))){
                seen.remove(s.charAt(left++));
            }
            
            seen.add(s.charAt(j));
            size = Math.max(size, j - left + 1);
            
        }
        return size;
        
    }
}