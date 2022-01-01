class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if(root1 is None and root2 is None): return None
        if(root1 is None):
            return root2
        if(root2 is None):
            return root1
        
        self.mergeNode(root1, root2)
        return root1
    
    # Always merging n1 to n2, if n1 is not none. 
    def mergeNode(self, n1, n2):
        # Both n1 and n2 are not none
        n1.val += n2.val
        # if((n1.left is None and n2.left is None):   
        # (n1.right is None and n2.right is None)):
        if(n1.left is None and n2.left is not None):
            print("Shouldn't reach here")
            n1.left = TreeNode(n2.left.val)
            return 
        if(n1.right is None and n2.right is not None):
            n1.right = TreeNode(n2.right.val)
            return 
            
        if(n1.left is not None and n2.left is not None):
            self.mergeNode(n1.left, n2.left)
        if(n2.right is not None and n2.right is not None):
            self.mergeNode(n1.right, n2.right)
            

def printTree(treeroot):
    frontier = [treeroot]
    pstr = ""
    while(bool(frontier)):
        nlevel = []
        for e in frontier:
            pstr += str(e.val)
            # print([v.val for v in frontier])    
            if(e.left is not None):
                nlevel.append(e.left)
                # print([v.val for v in nlevel])        
            if(e.right is not None):
                nlevel.append(e.right)
                # print([v.val for v in nlevel])        
        # print([v.val for v in nlevel])
        frontier = nlevel
    print(pstr)


if __name__ == '__main__':
    lnode4 = TreeNode(5)
    lnode3 = TreeNode(2)
    lnode2 = TreeNode(3, left = lnode4)
    lroot  = TreeNode(1, left = lnode2, right = lnode3)


    rnode7 = TreeNode(7)
    rnode5 = TreeNode(4)
    rnode3 = TreeNode(3, right=rnode7)
    rnode2 = TreeNode(1, right=rnode5)
    rroot  = TreeNode(2, left=rnode2, right=rnode3)
    
    solver =  Solution()
    # print(lnode3.val)
    # print(rnode3.val)
    # print(solver.mergeTrees(lroot, rroot).right.right.val)   
    printTree(solver.mergeTrees(lroot, rroot))