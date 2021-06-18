
# @Title: 打家劫舍 (House Robber)
# @Author: cocofe
# @Date: 2021-04-15 23:56:42
# @Runtime: 32 ms
# @Memory: 14.9 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        pprev, prev = 0, 0
        for idx, num in enumerate(nums):
            curr = max(prev, pprev+num)
            pprev, prev = prev, curr
        return prev
        dp[i] = max(dp[i-2] + num, dp[i-3] + num)
            ans = max(ans, dp[i])
        return ans
