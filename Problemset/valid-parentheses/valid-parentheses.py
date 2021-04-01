
# @Title: 有效的括号 (Valid Parentheses)
# @Author: cocofe
# @Date: 2020-01-10 23:40:46
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        char_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        if not s:
            return True
        for _s in s:
            if stack and stack[-1] == char_map.get(_s):
                stack.pop(-1)
            else:
                stack.append(_s)
        return bool(not stack)
            
        
