
# @Title: 包含min函数的栈 (包含min函数的栈 LCOF)
# @Author: cocofe
# @Date: 2020-09-12 20:54:02
# @Runtime: 148 ms
# @Memory: 16.4 MB

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self._stack:
            self._min_stack.append(x)
        else:
            _min = self._min_stack[-1]
            self._min_stack.append(min(_min, x))
        self._stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self._stack:
            self._min_stack.pop()
            return self._stack.pop()
        return None


    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1] if self._stack else None


    def min(self):
        """
        :rtype: int
        """
        return self._min_stack[-1] if self._min_stack else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
