"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
  """
  Assume:
  1 ---- 2         1: [2, 4]
  |      |         2: [1, 3]  
  |      |         3: [2, 4]
  4 ---- 3         4: [1, 3]
  
  =========================================================================================================
  Calling dfsClone(node):
   
  Call stack                    OC_map updates                                
  clone(1) ->                   1 => clone(1)                                 
    clone(2) ->                 2 => clone(2)                                  
      clone(1) ->               -                                             
      clone(3) ->               3 => clone(3)                                 
        clone(2) ->             -                      
        clone(4) ->             4 = > clone(4)
          clone(1) ->           -
          clone(3) ->.          -
  """
  def __init__(self):
    self.OC_map = {} # an original => clone maping

  def cloneGraph(self, node: 'Node') -> 'Node':
    if node is None: return None

    # if node is not cloned yet, clone the node 
    if node.val not in self.OC_map:
      clone = Node(node.val) 
      self.OC_map[node.val] = clone 
      for nei in node.neighbors:
        clone.neighbors.append(self.cloneGraph(nei))

    return self.OC_map[node.val]

      