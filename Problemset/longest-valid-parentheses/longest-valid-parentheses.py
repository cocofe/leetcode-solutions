
# @Title: 最长有效括号 (Longest Valid Parentheses)
# @Author: cocofe
# @Date: 2018-04-09 15:54:17
# @Runtime: 80 ms
# @Memory: N/A

class Solution(object):
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
                if idx - d[idx] > 0:
                    d[idx] += d[idx - d[idx]]
                left -= 1
            max_length = max(max_length, d[idx])
        return max_length
        
