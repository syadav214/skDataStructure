/*
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
*/

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        if(s.length() == 0 || s == null)   {
            return null;
        }
        List<String> dnaSeq = new ArrayList<>();
        HashMap<String,Integer> map = new HashMap<>();
        
        int i = 0;
        while(i+10 <= s.length()){
            String subSeq = s.substring(i, i+10);
            i++;
            map.put(subSeq, map.getOrDefault(subSeq, 0) + 1);
            if(map.get(subSeq) == 2){
                dnaSeq.add(subSeq);
            }
        }
        return dnaSeq;
    }
}
