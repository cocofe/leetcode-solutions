
# @Title: 用栈实现队列 (Implement Queue using Stacks)
# @Author: cocofe
# @Date: 2021-03-05 01:00:02
# @Runtime: 36 ms
# @Memory: 13.1 MB

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)

    def _transfer(self):
        for _ in range(len(self.push_stack)):
            num = self.push_stack.pop()
            self.pop_stack.append(num)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.pop_stack:
            self._transfer()
        return self.pop_stack.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.pop_stack:
            self._transfer()
        return self.pop_stack[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.pop_stack or self.push_stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
