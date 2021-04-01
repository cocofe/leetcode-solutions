
# @Title: 基本计算器 II (Basic Calculator II)
# @Author: cocofe
# @Date: 2021-03-11 01:26:42
# @Runtime: 116 ms
# @Memory: 16.8 MB

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(chars):
            stack = []
            prev_sign = '+'
            num = 0
            for idx, c in enumerate(chars):
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = helper(chars)
                elif c == ')':
                    break
                elif (not c.isdigit() and c != ' ') or idx == len(chars) - 1:
                    if prev_sign == '+':
                        stack.append(num)
                    elif prev_sign == '-':
                        stack.append(-num)
                    elif prev_sign == '*':
                        stack[-1] *= num
                    elif prev_sign == '/':
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    prev_sign = c
            return sum(stack)
        return helper(list(s))



