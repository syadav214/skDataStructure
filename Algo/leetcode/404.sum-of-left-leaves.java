/*
Given the root of a binary tree, return the sum of all left leaves.
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Leave means no child of the node.

 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        int[] sum = new int[1];
        return traverseForSum(root, sum, false);
    }
    
    public int traverseForSum(TreeNode root, int[] sum, boolean isLeft){      
        if(root == null){
            return 0;
        }
        
        if(root.left ==null && root.right ==null && isLeft) {
            sum[0] = sum[0] + root.val;
        }
        
        traverseForSum(root.left, sum, true);
        traverseForSum(root.right, sum, false);
        return sum[0];
    }
}
