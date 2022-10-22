# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, low, high) -> bool:
            # Base case. None is True --> every leaf node is a valid BST tree
            if root is None: return True
            
            if root.val >= high or root.val <= low:
                return False
        
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, high)
        
        return isValid(root, -float(inf), float(inf))