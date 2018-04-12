# coding=utf-8


class Solution(object):
    """
    Given an Array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    
    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}  # 用来索引指定值对应的位置
        for idx, val in enumerate(nums):
            least = target - val
            if least in tmp:
                return [tmp[least], idx]
            else:
                tmp[val] = idx




