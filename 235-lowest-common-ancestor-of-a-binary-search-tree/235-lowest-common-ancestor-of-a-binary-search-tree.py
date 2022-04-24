# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If p < root < q, then root is the LCA
        
        def recurse(node):
            if node.val <= p.val and node.val <= q.val: # p, q are in right subtree rooted at node
                if node.val == min(p.val, q.val):
                    return node
                else:
                    return recurse(node.right)
            elif node.val >= p.val and node.val >= q.val: # p, q are in left subtree rooted at node
                if node.val == max(p.val, q.val):
                    return node
                else:
                    return recurse(node.left)
            else:
                return node
        
        
        return recurse(root)
                