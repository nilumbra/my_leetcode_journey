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
        
        def recurse(node):
            if not node:
                return False
            
            left = recurse(node.left)
            right = recurse(node.right)
            mid = node == p or node == q
            
            if left + right + mid >= 2:
                self.ans = node
            
            return left or right or mid
        
        recurse(root)
        return self.ans