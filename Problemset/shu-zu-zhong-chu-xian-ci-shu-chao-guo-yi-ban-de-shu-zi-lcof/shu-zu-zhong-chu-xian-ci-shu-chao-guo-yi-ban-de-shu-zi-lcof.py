
# @Title: 数组中出现次数超过一半的数字 (数组中出现次数超过一半的数字  LCOF)
# @Author: cocofe
# @Date: 2020-08-13 00:40:38
# @Runtime: 24 ms
# @Memory: 13.4 MB

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums) / 2]
