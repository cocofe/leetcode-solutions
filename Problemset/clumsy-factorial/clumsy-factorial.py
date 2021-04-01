
# @Title: 笨阶乘 (Clumsy Factorial)
# @Author: cocofe
# @Date: 2021-04-01 22:18:11
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 要注意优先级, 碰到乘除法, 则直接取栈顶元素算结果, 如果是加减, 则放入栈中
        stack = []
        idx = 0
        for i in range(N, 0, -1):
            if not stack:
                stack.append(i)
            else:
                if idx == 0:
                    stack[-1] *= i
                elif idx == 1:
                    stack[-1] = int(stack[-1]/ float(i))
                elif idx == 2:
                    stack.append(i)
                else:
                    stack.append(-i)
                idx += 1
                idx %= 4
        return sum(stack)

