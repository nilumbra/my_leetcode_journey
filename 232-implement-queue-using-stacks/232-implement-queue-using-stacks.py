class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.s1) == 0:
            self.front = x
        self.s1.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
                
            return self.s2.pop()
        
        return self.s2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.s2) == 0:
            return self.front
        else:
            return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()