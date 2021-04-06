
# @Title: 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)
# @Author: cocofe
# @Date: 2021-04-07 01:20:38
# @Runtime: 44 ms
# @Memory: 14.9 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:
                if nums[right] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = mid
        return nums[left]


