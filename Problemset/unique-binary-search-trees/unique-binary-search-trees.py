
# @Title: 不同的二叉搜索树 (Unique Binary Search Trees)
# @Author: cocofe
# @Date: 2020-12-27 03:23:05
# @Runtime: 12 ms
# @Memory: 12.9 MB

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]

