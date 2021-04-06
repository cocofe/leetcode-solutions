
# @Title: 搜索旋转排序数组 II (Search in Rotated Sorted Array II)
# @Author: cocofe
# @Date: 2021-04-07 01:08:48
# @Runtime: 40 ms
# @Memory: 15.3 MB

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            # 跳过重复数字, 避免[1,0,1,1,1] 判断mid与left是否在同一侧时候无法判断
            # 只有left和right可以重复, 除非mid==right或者mid==left, 否则mid值与left,right不同
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while right > left and nums[right] == nums[right-1]:
                right -= 1
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            # [3,3,2, 1]
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
        return False
