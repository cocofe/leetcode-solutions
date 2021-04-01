
# @Title: 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)
# @Author: cocofe
# @Date: 2021-03-28 16:26:50
# @Runtime: 24 ms
# @Memory: 13.3 MB

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            print left, right, mid
            # left 和 mid 在同一侧
            if nums[left] <= nums[mid]:
                # 对于 left = mid = right 情况, right 会小于 left 会break
                if nums[right] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = mid
        return nums[left]
