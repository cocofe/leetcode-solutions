
# @Title: 完全平方数 (Perfect Squares)
# @Author: cocofe
# @Date: 2021-04-27 00:27:25
# @Runtime: 5052 ms
# @Memory: 15.4 MB

class Solution:
    def numSquares(self, n: int) -> int:
        # 缓存完全平方数
        cache = {i: i**2 for i in range(1, int(n ** 0.5) + 1)}
        dp = collections.defaultdict(lambda: float('inf'))
        for i in range(1, n+1):
            base = int(i ** 0.5)
            if cache[base] == i:
                dp[i] = 1
            else:
                for j in range(base, 0, -1):
                    dp[i] = min(dp[i], 1 + dp[i - cache[j]])
        return dp[n]
