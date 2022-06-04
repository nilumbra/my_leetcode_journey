# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head, last_node = None, None
        ptr = head
        
        while ptr:
            next_node = ptr.next # next_node --> ptr.next (ref)
            
            # insert ptr before the "old new_head", and now new_head is ptr
            new_head, ptr.next = ptr, new_head 
            
            ptr = next_node
        
        return new_head