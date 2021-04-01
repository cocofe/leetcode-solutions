
# @Title: 三步问题 (Three Steps Problem LCCI)
# @Author: cocofe
# @Date: 2020-09-20 14:25:05
# @Runtime: 1404 ms
# @Memory: 113.8 MB

class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {
            0: 1,
            1: 1
            
        }
        for i in range(2, n+1):
            dp[i] = 0
            for step in range(1, 4):
                if i - step < 0:
                    break
                dp[i] += dp[i-step]
            dp[i] %= 1000000007
        return dp[n]

