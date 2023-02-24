# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      # Node A is an LCA of p and q, 
      #   if p is in the left subtree of A and q is in the right subtree of A
      
      # algorithm:
      # if node A is a common ancestor of p and q, not(A == q A == p):
      #   check: rl <- p,q is in left subtree, or rr <- p, q is in right subtree:
      #     if (p, q) are both in left subtree, we recurse on left subtree
      #     or if ... in right ..., we recurse on right
      #     if either is not true, then node A is a common ancestor or p and q
      
      def r(root):
        """
        Report if subtree rooted at root contains 0, 1, or 2 target nodes.
        
        """
        if not root: return 0
        
        left = r(root.left)
        if left >= 2: return 
        right = r(root.right)
        
        curr = root == p or root == q
        #print(root.val, left + right + curr, root.val == p, root.val == q)
        if left + right + curr >= 2:
          self.ans = root 
          
        
        return left or right or curr
        

      r(root)
      return self.ans