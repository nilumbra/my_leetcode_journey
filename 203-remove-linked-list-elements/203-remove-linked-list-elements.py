# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        def recurse(ptr):
            if ptr is None: 
                return None
            elif ptr.val == val:
                return recurse(ptr.next)
            else:
                ptr.next = recurse(ptr.next)
                return ptr
            
        
        return recurse(head)