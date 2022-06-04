class ListNode:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt 
        
class MyLinkedList(object):
    def __init__(self):
        self.fakehead = ListNode()
        self.l = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index + 1 > self.l: return -1
        i = 0
        ptr = self.fakehead.next # start from the true head
        while ptr:
            if i == index:
                return ptr.val
            i += 1
            ptr = ptr.next
            
        raise IndexError("MyLinkedList index out of range!!")
        
        
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        curr_head = self.fakehead.next
        self.fakehead.next = ListNode(val, curr_head)
        self.l += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        
        ptr = self.fakehead.next
        if ptr is None:
            self.fakehead.next = new_node
        else:
            while ptr.next:
                ptr = ptr.next
        
            # ptr is the last node of the linked list now
            ptr.next = new_node
            
        self.l += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.l:
            self.addAtTail(val)
        elif index > self.l:
            return
        else:
            assert index >= 0, "Invalid index!"
            ptr = self.fakehead.next
            i = 0
            
            previous_node = self.fakehead
            while i < index:
                # print(i, ptr.val)
                previous_node = previous_node.next
                ptr = ptr.next
                i += 1
            
            new_node = ListNode(val, ptr)
            previous_node.next = new_node
            self.l += 1                
                
            

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if 0 <= index < self.l:
            previous_node = self.fakehead
            ptr = self.fakehead.next
            i = 0
            while i < index:
                previous_node = previous_node.next
                ptr = ptr.next
                i += 1
            
            # ptr -> i-node
            # previous_node -> (i-1)-node
            previous_node.next = ptr.next
            
            self.l -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)