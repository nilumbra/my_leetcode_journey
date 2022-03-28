# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = None
        knode_ = head
        
        knode = ListNode() # placeholder
        knode.next = knode_
        
        # Separate the first reverse, to get the return new_head
        if is_reverse_k_possible(knode_, k):
            new_head, knode, knode_ = reverse_k_group(knode, knode_, k)
            
        while is_reverse_k_possible(knode_, k):
            knode, knode_ = reverse_k_group(knode, knode_, k)[1:]
        
        return new_head
    
def link_backward(cur, cur_):
        """
        Assumes n1, n2 are adjacent nodes in a k-group and originally n1.next == n2 
        Links them the other way then
        returns the reference to the old n2.next, i.e. n3, and n2
        """
        cur__ = cur_.next
        cur_.next = cur
        return (cur_, cur__)    
    
def reverse_k_group(n0, n1, k):
        """
        Return cur, cur_, which is the k-th and (k+1)-th node respectively
        e.g.
        
        n0 = ListNode()
        n0.next = n1
        reverse_k_group(n0, n1, 2)   
        n1-->n2-->n3-->n4-->n5  ->  (n0-->)n2-->n1-->n3-->n4-->n5  
        
        reverse_k_group(n1, n3, 2)  
        (n0-->)n2-->n1-->n3-->n4-->n5  ->  (n0-->)n2-->n1-->n4-->n3-->n5
        """
        new_tail = n1
        cur, cur_ = n1, n1.next
        for i in range(k - 1):
            cur, cur_ = link_backward(cur, cur_)
            
        n0.next = cur 
        new_tail.next = cur_
        return (cur, new_tail, cur_)
        
def is_reverse_k_possible(head, k):
    if not head: return False
    for i in range(k - 1):
        if head.next is None: 
            return False
        else:
            head = head.next
    return True    
            
    
    
    
    
        