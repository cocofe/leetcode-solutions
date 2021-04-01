
# @Title: 删除有序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: cocofe
# @Date: 2020-11-06 23:36:21
# @Runtime: 20 ms
# @Memory: 14 MB

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 1
        count = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
                count += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return len(nums) - count
