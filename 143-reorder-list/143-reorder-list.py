# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find the middle node
        # If there are two middle node, find the second one
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        # Reverse 
        # convert 1->2->3->4->5 into 1->2->3, 5->4->3
        # convert 1->2->3->4->5->6 into 1->2->3->4, 6->5->4  
        prev, ptr = None, slow
        while ptr:
            ptr.next, prev, ptr = prev, ptr, ptr.next
             
        
        # merge two lists
        ptr = head
        rptr = prev
        while rptr.next:
            ptr.next, ptr = rptr, ptr.next
            rptr.next, rptr = ptr, rptr.next
        
        
        return head