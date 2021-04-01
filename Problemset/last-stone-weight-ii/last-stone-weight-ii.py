
# @Title: 最后一块石头的重量 II (Last Stone Weight II)
# @Author: cocofe
# @Date: 2020-12-25 02:50:50
# @Runtime: 52 ms
# @Memory: 14.4 MB

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total_sum = sum(stones)
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        for i, stone in enumerate(stones):
            for size in range(total_sum / 2 + 1):
                if stone > size:
                    dp[i][size] = dp[i-1][size]
                else:
                    dp[i][size] = max(dp[i-1][size], dp[i-1][size-stone]+stone)
        # print dp[len(stones)-1][(total_sum + 1) / 2 - 1], total_sum
        return abs(total_sum - 2*dp[len(stones)-1][total_sum / 2])
