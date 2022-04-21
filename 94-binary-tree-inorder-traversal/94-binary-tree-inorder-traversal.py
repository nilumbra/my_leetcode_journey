# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Is left child of the node is None? No. Then go left.
        # Go right till you meet None or current node(t)
        
        # MEET NONE:
        # 1. Add node to output
        # 2. Link predecessor.right = node 
        # 3. t = t.l
        out = []
        while root:
            if not root.left:
                out.append(root.val)
                root = root.right
            else:
                ptr = root.left
                while ptr.right and ptr.right != root: 
                    ptr = ptr.right
                    
                if not ptr.right:
                    ptr.right = root
                    root = root.left
                else: # ptr.right == t
                    out.append(root.val)
                    ptr.right = None
                    root = root.right

        return out
                
        