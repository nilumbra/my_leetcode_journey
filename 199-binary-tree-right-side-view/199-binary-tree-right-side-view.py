# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depth = 0
        rightV = []
        def addRightV(node):
            nonlocal depth, rightV
            if node is not None:
                depth += 1
                if depth > len(rightV):
                    rightV.append(node.val)
                    
                addRightV(node.right)
                addRightV(node.left)
                depth -= 1
           
        addRightV(root)
        return rightV