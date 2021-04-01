
# @Title: 在排序数组中查找元素的第一个和最后一个位置 (Find First and Last Position of Element in Sorted Array)
# @Author: cocofe
# @Date: 2021-03-03 00:17:23
# @Runtime: 24 ms
# @Memory: 13.5 MB

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid - 1
        l_ans = left if left < len(nums) and nums[left] == target else -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        r_ans = left - 1 if 0 <= left - 1 < len(nums) and nums[left - 1] == target else -1
        return [l_ans, r_ans]

