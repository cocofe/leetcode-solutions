
# @Title: 打家劫舍 (House Robber)
# @Author: cocofe
# @Date: 2020-12-17 21:48:46
# @Runtime: 16 ms
# @Memory: 12.9 MB

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            dp[i] = max(dp[i-2] + num, dp[i-3] + num)
            ans = max(ans, dp[i])
        return ans
