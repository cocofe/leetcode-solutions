
# @Title: 0～n-1中缺失的数字 (缺失的数字  LCOF)
# @Author: cocofe
# @Date: 2021-03-01 21:45:52
# @Runtime: 20 ms
# @Memory: 13.9 MB

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
