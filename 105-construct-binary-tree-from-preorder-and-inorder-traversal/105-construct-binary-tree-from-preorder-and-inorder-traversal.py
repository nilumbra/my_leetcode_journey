# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def restoreTree(left, right):
            nonlocal curr
            # print(f'curr index: {curr}')
            if left >= right:
                return None
            
            root_val = preorder[curr]
            root = TreeNode(val=root_val)
            
            curr += 1
            
            _ = M[root_val]
            
            root.left = restoreTree(left, _)
            root.right = restoreTree(_ + 1, right)

            return root
            
        curr = 0 # preorder_index; the index of the preorder value to add to curr node
        M = {v: i for i, v in enumerate(inorder)}
            

        # print(f'list len:{len(preorder)}')
            
        return restoreTree(0, len(preorder))