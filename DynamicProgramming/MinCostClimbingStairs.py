# -*- coding: UTF-8 -*-
class Solution(object):
    """
    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

    Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
    
    Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
    Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
    Note:
    cost will have a length in the range [2, 1000].
    Every cost[i] will be an integer in the range [0, 999].

    """
    def minCostClimbingStairs(self, cost):
        """
        这边唯一的坑就是, 爬最后一个楼梯的时候,可以直接从倒二个楼梯结束,所以
        dp[0], dp[1] = cost[0], cost[1]
        dp[i] = min(dp[i-1]+val, dp[i-2]+val) i > 1
        ret =  min(dp[-1], dp[-2])
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        dp = [0] * length
        for idx, val in enumerate(cost):
            if idx == 0 or idx == 1:
                dp[idx] = val
            else:
                dp[idx] = min(dp[idx - 1] + val, dp[idx - 2] + val)
        return min(dp[-1], dp[-2])