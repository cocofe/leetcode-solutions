# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
    
    For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
    the contiguous subarray [4,-1,2,1] has the largest sum = 6.
    """
    def maxSubArray(self, nums):
        """
        求子数组的最大和
        :type nums: List[int]
        :rtype: int
        """
        ans, ret = 0, 0
        for x in nums:
            if ans + x < 0:
                ans = 0
            else:
                ans += x
                ret = max(ret, ans)
        if ret == 0:
            return max(nums)
        else:
            return ret