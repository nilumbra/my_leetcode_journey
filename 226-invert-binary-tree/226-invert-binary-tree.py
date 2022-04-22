# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invertRecursively(tree):
            """
            Invert the tree rooted at <tree>
            """
            if tree:
                tree.left, tree.right = tree.right, tree.left
                invertRecursively(tree.right)
                invertRecursively(tree.left)
            
        invertRecursively(root)
        return root
            