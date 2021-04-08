
# @Title: 用两个栈实现队列 (用两个栈实现队列 LCOF)
# @Author: cocofe
# @Date: 2021-04-09 01:11:41
# @Runtime: 372 ms
# @Memory: 18.7 MB

class CQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []


    def appendTail(self, value: int) -> None:
        self.push_stack.append(value)


    def deleteHead(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop() if self.pop_stack else -1
        



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
