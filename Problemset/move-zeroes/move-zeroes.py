
# @Title: 移动零 (Move Zeroes)
# @Author: cocofe
# @Date: 2020-08-13 13:33:00
# @Runtime: 24 ms
# @Memory: 13.3 MB

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0
        to_processing_idx = 0
        while idx < len(nums):
            p = nums[idx]
            if p == 0:
                idx += 1
                continue
            if idx != to_processing_idx:
                nums[to_processing_idx] = nums[idx]
            idx += 1
            to_processing_idx += 1
        for i in range(to_processing_idx, len(nums)):
            nums[i] = 0

