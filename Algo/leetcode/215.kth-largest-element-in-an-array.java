/*
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
*/

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> meanHeap = new PriorityQueue<>();
        for(int i : nums){
            meanHeap.add(i);
            if(meanHeap.size() > k){
                meanHeap.remove();
            }
        }
        return meanHeap.remove();
    }
}