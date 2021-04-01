
# @Title: 搜索旋转排序数组 (Search in Rotated Sorted Array)
# @Author: cocofe
# @Date: 2021-03-28 16:50:49
# @Runtime: 24 ms
# @Memory: 13 MB

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return -1
