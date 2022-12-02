# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ######## 110. Balanced Binary Tree ###########
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
    ##############################################
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedArray = []
    
        # Inorder traverse BST and populate them in an array ascendingly
        def inorder_set(node: TreeNode):
            # nonlocal sortedArray
            if node:
                inorder_set(node.left)
                sortedArray.append(node)
                inorder_set(node.right)
                
        # Divide and conquer:
        # 1. select the mid of the original array A[mid]
        # 2. A[start: mid - 1] is the left subtree and A[mid + 1: end] is the right subtree
        #    This way, the resulted tree will always be balanced, as len(A[start: mid - 1]) and len(A[mid + 1: end]) is
        #    guarenteed to differ by less 1
        # 3. Build the two subtrees 
        def buildBalancedBST(start:int, end:int):
            # nonlocal sortedArray
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
            
        if self.isBalancedBST(root):
            return root
        else: 
            inorder_set(root)
            return buildBalancedBST(0, len(sortedArray) - 1)
        
        