# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        else:
            return self.setBSTNode(nums, 0, len(nums))
        
    def setBSTNode(self, nums: List[int], left, right) -> TreeNode:
        root = TreeNode()
        if left < right:
            mid = (left + right) // 2
            root.val = nums[mid]
            root.left = self.setBSTNode(nums, left, mid)
            root.right = self.setBSTNode(nums, mid + 1, right)
            
            return root   
            
            
        