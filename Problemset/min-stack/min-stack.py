
# @Title: 最小栈 (Min Stack)
# @Author: cocofe
# @Date: 2020-08-13 13:11:15
# @Runtime: 136 ms
# @Memory: 16.1 MB

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        _min = self.min_stack[-1] if self.min_stack else None
        to_push_val = x if _min is None else min(x, _min)
        self.min_stack.append(to_push_val)            



    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
