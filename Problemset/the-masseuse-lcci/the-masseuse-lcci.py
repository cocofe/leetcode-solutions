
# @Title: 按摩师 (The Masseuse LCCI)
# @Author: cocofe
# @Date: 2020-09-20 15:29:35
# @Runtime: 16 ms
# @Memory: 12.3 MB

class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = {
            -1: 0,
            0: nums[0],
        }
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]
