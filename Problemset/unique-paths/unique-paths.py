
# @Title: 不同路径 (Unique Paths)
# @Author: cocofe
# @Date: 2018-04-09 16:34:47
# @Runtime: 33 ms
# @Memory: N/A

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        for row in range(m):
            for col in range(n):
                if col - 1 >= 0:
                    dp[col] += dp[col - 1]
        return dp[n-1]
