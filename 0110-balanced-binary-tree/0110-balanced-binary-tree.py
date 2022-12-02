

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    return self.traverse(root)[1]
  
  def traverse(self, root):
    if root:
      lh, isBL = self.traverse(root.left)
      rh, isBR = self.traverse(root.right)
      
      if abs(lh - rh) <= 1 and isBL and isBR:
        return max(lh, rh) + 1, True
      else:
        return max(lh, rh) + 1, False
    else:
      return 0, True