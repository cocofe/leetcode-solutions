
# @Title: 搜索旋转排序数组 (Search in Rotated Sorted Array)
# @Author: cocofe
# @Date: 2021-04-07 00:59:14
# @Runtime: 36 ms
# @Memory: 15.2 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            # [3,3,2, 1]
            # 可能mid==left
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
          left = mid + 1
                    
        return -1
