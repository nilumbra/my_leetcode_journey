# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, ub, lb):
            # Base case. None is True --> every leaf node is a valid BST tree
            if root is None: return True
            
            if ub is not None and root.val >= ub.val or lb is not None and root.val <= lb.val:
                return False
        
            return isValid(root.left, root, lb) and isValid(root.right, ub, root)
        
        return isValid(root, None, None)