# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack_pathsum(node, currSum):
            """
            Try to sum every root-to-leaf path of the tree using backtraking toward the <targetSum>
            Return True if such path exists, otherwise return False
            """
            if not node:
                return False
            
            currSum += node.val
            
            if not node.left and not node.right: # If node is a leaf 
                return currSum == targetSum
            else:
                return backtrack_pathsum(node.left, currSum) or backtrack_pathsum(node.right, currSum)
        
        return backtrack_pathsum(root, 0)