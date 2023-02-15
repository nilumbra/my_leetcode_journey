class SegmentTreeNode:
  def __init__(self, left = None, right = None, leftBound: int = 0, rightBound: int = 0, val: int = 0, parent = None):
    self.left = left
    self.right = right
    self.val = val # visualizing the tree as an array A(in its traversal order), val = sum(A[left: right])
    self.leftBound = leftBound
    self.rightBound = rightBound
  # Get the segment tree leave 
    self.parent = parent 


  def __getitem__(self, key):
    """
    Recurrence assumption: self.leftBound <= key <= self.rightBound, raise IndexError if not
    """
    if key < self.leftBound or key > self.rightBound:
      raise IndexError('The given key is not in this segment tree!!')
    
    if self.leftBound == self.rightBound and self.leftBound == key:
      # print(self)
      return self
    
    if self.left.leftBound <= key <= self.left.rightBound: # may in left node
      return self.left.__getitem__(key)
    else:
      return self.right.__getitem__(key)

  def __setitem__(self, key, val:int):
    """
    Recurrence assumption: self.leftBound <= key <= self.rightBound, raise IndexError if not
    """
    if key < self.leftBound or key > self.rightBound:
      raise IndexError('The given key is not in this segment tree!!')
    

    if self.leftBound == self.rightBound and self.leftBound == key:
      # print('Setting node:', self, 'Set value = ', val)
      d = val - self.val # the difference to add to current node
      self.val += d
      
      # proprogate the diff
      curr = self
      while curr.parent:
        # print('Propagating diff:', curr.parent, 'before val = ', curr.parent.val)
        curr.parent.val += d
        # print('Propagating diff:', curr.parent, 'after val = ', curr.parent.val)
        curr = curr.parent
      return 

    # print('Passing node:', self)
    if self.left.leftBound <= key <= self.left.rightBound: # may in left node
      self.left.__setitem__(key, val)
    else:
      self.right.__setitem__(key, val)


  def sumRange(self, left:int, right: int):
    """
    Given a range(=[left, right]), return sum in range. 
    Trim the given range if necessary.
    """
    assert left <= right
    if self.leftBound == left and self.rightBound == right:
      return self.val


    ## lrtrim in case the given 
    left = max(self.leftBound, left)
    right = min(self.rightBound, right) 

    if self.right.leftBound <= left:  # [left, right] is in right's range
      return self.right.sumRange(left, right)
    elif self.left.rightBound >= right:
      return self.left.sumRange(left, right) # [left, right] is in left's range
    else:
      return self.left.sumRange(left, self.left.rightBound) + self.right.sumRange(self.right.leftBound, right)

  def __repr__(self):
    return f'SegmentTreeNode:\n==================\nrange = [{self.leftBound}, {self.rightBound}]\nrangeSum = {self.val}\n=================='
  
class SegmentTree:
  def __init__(self, root: SegmentTreeNode = None):
    self.root = root
  
  @classmethod
  def build_tree(cls, arr):
    root = cls.build_node(0, len(arr) - 1, arr, SegmentTreeNode(leftBound=0, rightBound=len(arr) - 1))
    return cls(root)
  
  @classmethod
  def build_node(cls, leftIndex, rightIndex, arr, node):
    """
    Given leftIndex, rightIndex,
    """
    if leftIndex == rightIndex:
      node.val = arr[leftIndex]
      return node
    
    
    mid = (leftIndex + rightIndex) // 2 
    
    node.left = cls.build_node(leftIndex, mid, arr, SegmentTreeNode(leftBound=leftIndex, rightBound=mid, parent=node))
    node.right = cls.build_node(mid + 1, rightIndex, arr, SegmentTreeNode(leftBound=mid+1, rightBound=rightIndex, parent=node)) 
    node.val = node.left.val + node.right.val
    return node
  
  def leavesIterator(self):
    def r(root):
      if root.left == None and root.right == None:
        yield root.val
      else:
        yield from r(root.left)
        yield from r(root.right)

    return r(self.root) # return the iterator

  def __setitem__(self, key, val: int):
    self.root[key] = val
    
    
      
class NumArray:
  def __init__(self, nums: List[int]):
    self.tree = SegmentTree.build_tree(nums) 
    print(list(self.tree.leavesIterator()))
    
  def update(self, index: int, val: int) -> None:
    self.tree[index] = val

  def sumRange(self, left: int, right: int) -> int:
    return self.tree.root.sumRange(left, right)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)