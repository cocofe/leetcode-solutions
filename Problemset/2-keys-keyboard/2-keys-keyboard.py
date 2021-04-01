
# @Title: 只有两个键的键盘 (2 Keys Keyboard)
# @Author: cocofe
# @Date: 2020-09-06 15:22:39
# @Runtime: 160 ms
# @Memory: 12.5 MB

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            minus = i / 2
            to_divider = 1
            for x in range(minus, 0, -1):
                if i % x == 0:
                    to_divider = x
                    break
            dp[i] = dp[to_divider] + (i / to_divider)
        return dp[n]

