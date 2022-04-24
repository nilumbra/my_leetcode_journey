# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        onums = set()
        
        def traverse(node):
            if not node:
                return False
            elif node.val in onums:
                return True
            else:
                onums.add(k - node.val)
                return traverse(node.left) or traverse(node.right)
        
                        
        return traverse(root)