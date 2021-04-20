
# @Title: 栈的压入、弹出序列 (栈的压入、弹出序列 LCOF)
# @Author: cocofe
# @Date: 2021-04-18 07:24:18
# @Runtime: 44 ms
# @Memory: 14.8 MB

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx = 0
        for num in pushed:
            if num == popped[idx]:
                idx += 1
                while stack and idx < len(popped) and stack[-1] == popped[idx]:
                    idx += 1
                    stack.pop()
            else:
                stack.append(num)
        return idx == len(popped)
