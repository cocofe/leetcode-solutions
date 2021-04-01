
# @Title: 最长连续递增序列 (Longest Continuous Increasing Subsequence)
# @Author: cocofe
# @Date: 2020-12-27 01:59:33
# @Runtime: 28 ms
# @Memory: 13.9 MB

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ans = 1
        i, j = 0, 1
        while j < len(nums):
            # print i, j, ans
            if nums[j] <= nums[j-1]:
                i = j
            ans = max(j - i + 1, ans)
            j += 1
        return ans

