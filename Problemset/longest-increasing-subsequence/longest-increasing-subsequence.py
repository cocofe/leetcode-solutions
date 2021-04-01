
# @Title: 最长递增子序列 (Longest Increasing Subsequence)
# @Author: cocofe
# @Date: 2020-12-27 01:44:24
# @Runtime: 2568 ms
# @Memory: 13.6 MB

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(lambda: 1)
        ans = 1
        for i, num in enumerate(nums):
            j = i - 1
            choices = []
            while j >= 0:
                if nums[j] < num:
                    choices.append(j)
                j -= 1
            if choices:
                dp[i] = max([dp[j] for j in choices]) + 1
            ans = max(dp[i], ans)
        return ans
        
