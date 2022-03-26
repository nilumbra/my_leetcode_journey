# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        # l1_end = False
        # l2_end = False
        l3 = ListNode(-1)
        l3_head = l3

        while not(not l1 and not l2 and carry == 0):
            cur = ListNode(0)
            if(not l1 and not l2):
                cur.val = 1
                l3.next = cur
                return l3_head.next
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry 
            if s >= 10:
                s = s - 10
                carry = 1
            else:
                carry = 0
            cur.val = s 
            l3.next = cur
 
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            l3 = l3.next if l3 else l3
        
        return l3_head.next
        