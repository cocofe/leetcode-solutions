
# @Title: 删除有序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: cocofe
# @Date: 2021-04-18 06:40:52
# @Runtime: 32 ms
# @Memory: 15.7 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p, fast_p = 0, 1
        while fast_p < len(nums):
            if nums[p] != nums[fast_p]:
                nums[p+1] = nums[fast_p]
                p += 1
                fast_p += 1
            else:
                fast_p += 1 
        return p + 1


     slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return len(nums) - count
