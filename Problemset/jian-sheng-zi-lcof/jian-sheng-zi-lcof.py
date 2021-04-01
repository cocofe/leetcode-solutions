
# @Title: 剪绳子 (剪绳子  LCOF)
# @Author: cocofe
# @Date: 2020-10-24 23:56:39
# @Runtime: 20 ms
# @Memory: 13.2 MB

class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {
            1: 1
        }
        for i in range(2, n+1):
            step = 1
            _max = float('-inf')
            while i - step > 0:
                _max = max(max(dp[i-step], i-step) * step, _max)
                step += 1
            dp[i] = _max
        return dp[n]

