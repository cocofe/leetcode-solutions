
# @Title: 连续数列 (Contiguous Sequence LCCI)
# @Author: cocofe
# @Date: 2020-09-20 15:20:41
# @Runtime: 24 ms
# @Memory: 13 MB

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
