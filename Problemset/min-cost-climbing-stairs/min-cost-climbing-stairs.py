
# @Title: 使用最小花费爬楼梯 (Min Cost Climbing Stairs)
# @Author: cocofe
# @Date: 2020-12-21 20:39:06
# @Runtime: 40 ms
# @Memory: 13.2 MB

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        for i, cos in enumerate(cost):
            dp[i] = min(dp[i-1], dp[i-2]) + cos
        return min(dp[len(cost)-1], dp[len(cost)-2])
