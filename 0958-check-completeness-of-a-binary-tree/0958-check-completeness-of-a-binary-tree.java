/**
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
    public boolean isCompleteTree(TreeNode root) {
      Queue<TreeNode> q = new LinkedList<>();
      q.add(root);
      
      boolean lastLevel = false;
      while (!q.isEmpty()) {
        int ln = q.size();
        // System.out.println("lv n:" + ln);
        if (lastLevel) {
          for (int i = 0; i < ln; i++) {
            TreeNode node = q.poll();
            // make sure every node doesn't have children
            if (node.left != null || node.right != null) return false;
          }
          continue;
        }
        
        for (int i = 0; i < ln; i++) {
          TreeNode node = q.poll();
          // System.out.println(node.val);
          if (node.left == null) {
            lastLevel = true;
          } else {
            if (lastLevel) return false; 
            q.add(node.left);
            // System.out.println("node " + node.val + " adding " + node.left.val);
          } 
          
          if (node.right == null) {
            lastLevel = true;
          } else {
            if (lastLevel) return false;
            q.add(node.right);
            // System.out.println("node " + node.val + " adding " + node.right.val);
          }
          
        }
      }
      
      return true;
    }
}