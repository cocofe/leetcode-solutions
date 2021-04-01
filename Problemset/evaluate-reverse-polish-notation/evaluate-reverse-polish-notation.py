
# @Title: 逆波兰表达式求值 (Evaluate Reverse Polish Notation)
# @Author: cocofe
# @Date: 2021-03-20 23:50:33
# @Runtime: 44 ms
# @Memory: 14.4 MB

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            
            if token not in ['/', '-', '+', '*']:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '/':
                    stack.append(int(float(b) / a))
                elif token == '*':
                    stack.append(b * a)
                elif token == '+':
                    stack.append(b + a)
                else:
                    stack.append(b - a)
        return stack[0]
