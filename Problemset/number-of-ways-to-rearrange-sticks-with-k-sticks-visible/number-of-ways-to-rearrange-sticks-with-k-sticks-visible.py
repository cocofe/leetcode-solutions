
# @Title: 恰有 K 根木棍可以看到的排列数目 (Number of Ways to Rearrange Sticks With K Sticks Visible)
# @Author: cocofe
# @Date: 2021-05-18 01:57:59
# @Runtime: 3844 ms
# @Memory: 88.5 MB

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        # 每次取最大值, 选择位置安放(这个值在已有的排列中是最小的!!!)
        # 放在最前面, 这个一定会被看到(这个值一定是k), 所以 他的排列个数为 dp[n-1][k-1]
        # 不放在最前面,  则他一定看不到, 有n-1中放法, 所以他的排列个数为 (n-1) * dp[n-1][k]
        # dp[n][k] = dp[n-1][k-1] + (n-1) * dp[n-1][k]
        dp[0][0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j-1] + (i-1) * dp[i-1][j]) % MOD
        return dp[n][k]
        
        
