class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = []
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.mini:
            self.mini.append(x)
        else:
            self.mini.append(min(x,self.mini[-1]))
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.mini.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.mini[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
