
# @Title: 删除有序数组中的重复项 II (Remove Duplicates from Sorted Array II)
# @Author: cocofe
# @Date: 2021-04-06 23:03:48
# @Runtime: 48 ms
# @Memory: 14.9 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        p, fast_p = 0, 1
        while fast_p < len(nums):
            if nums[fast_p] != nums[p] or ((p-1 >= 0 and nums[p] != nums[p-1]) or p - 1 < 0):
                p += 1
                nums[p] = nums[fast_p]
            fast_p += 1
        return p + 1
