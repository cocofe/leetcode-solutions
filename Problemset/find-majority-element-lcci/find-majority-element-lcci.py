
# @Title: 主要元素 (Find Majority Element LCCI)
# @Author: cocofe
# @Date: 2020-10-28 22:58:28
# @Runtime: 16 ms
# @Memory: 14.1 MB

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums = sorted(nums)
        mid = nums[length / 2]
        mid_count = 0
        for num in nums:
            if num == mid:
                mid_count += 1
        return mid if mid_count > length / 2 else -1
