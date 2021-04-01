
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: cocofe
# @Date: 2018-04-13 11:17:03
# @Runtime: 41 ms
# @Memory: N/A

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for x in range(2,n+1):
            dp[x] = dp[x-1] + dp[x-2]
        return dp[n]
        
