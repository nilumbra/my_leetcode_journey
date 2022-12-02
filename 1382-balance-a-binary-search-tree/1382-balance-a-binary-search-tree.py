# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isBalancedBST(self, root) -> bool:
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
    
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedArray = []
        def find_min(node:TreeNode) -> TreeNode:
            while node.left:
                node = node.left
            
            return node
        
        def inorder_set(node: TreeNode):
            nonlocal sortedArray
            if node:
                inorder_set(node.left)
                sortedArray.append(node)
                inorder_set(node.right)
                
        def buildBalancedBST(start:int, end:int):
            nonlocal sortedArray
            if start < end:
                mid = (start+end) // 2
                root = sortedArray[mid]
                # print(start, mid, end)
                root.left = buildBalancedBST(start, mid - 1)
                root.right = buildBalancedBST(mid + 1, end)
                return root
            elif start == end:
                root = sortedArray[start]
                root.left = None
                root.right = None
                return root
            else:
                return None
            
            # pick mid
            # set as root
            # sorted_array[0: mid] 
            # sorted_array[mid]
#         def bstIterator(node: TreeNode):
#             while (nxt := nextLarger(node)):
#                 yield nxt
#                 node = nxt
        if self.isBalancedBST(root):
            return root
        else: 
            inorder_set(root)
            return buildBalancedBST(0, len(sortedArray) - 1)
            
            # min_node = find_min(root)
            # sortedArray = list(bstIterator(min_node))
        
        