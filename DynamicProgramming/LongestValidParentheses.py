# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    For "(()", the longest valid parentheses substring is "()", which has length = 2.

    Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
    """
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0] * len(s)
        max_length = 0
        left = 0
        for idx, x in enumerate(s):
            if x == '(':
                left += 1
            elif x == ')' and left > 0:
                d[idx] = 2 + d[idx - 1]
                # if idx - d[idx] > 0:
                d[idx] += d[idx - d[idx]]
                left -= 1
            max_length = max(max_length, d[idx])
        return max_length

    def test(self):
        s = "()(())"
        # s = "()()"
        # s = "()"
        print self.longestValidParentheses(s)