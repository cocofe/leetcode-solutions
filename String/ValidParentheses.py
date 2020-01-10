# -*- coding: UTF-8 -*-


class Solution(object):
    """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.

        Example 1:

        Input: "()"
        Output: true
        Example 2:

        Input: "()[]{}"
        Output: true
        Example 3:

        Input: "(]"
        Output: false
        Example 4:

        Input: "([)]"
        Output: false
        Example 5:

        Input: "{[]}"
        Output: true
    """
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

