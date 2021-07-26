
# @Title: 使用最小花费爬楼梯 (Min Cost Climbing Stairs)
# @Author: cocofe
# @Date: 2021-07-24 18:00:42
# @Runtime: 48 ms
# @Memory: 14.8 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            tmp = a
            a = b
            b = min(tmp, b) + cost[i]
        return min(a, b)
