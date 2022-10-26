# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def isCyclic(slow, fast):
    if fast is None:
        return None
    
    while fast.next and fast.next.next:            
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return slow

    return None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head;
        slow = head;
        
        intersection = isCyclic(slow, fast)
        if intersection is None:
            return None
        else:
            s = head
            while intersection is not s:
                s = s.next
                intersection = intersection.next
            
            return s
            
        