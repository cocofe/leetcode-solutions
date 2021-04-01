
# @Title: 乘积最大子数组 (Maximum Product Subarray)
# @Author: cocofe
# @Date: 2018-04-19 22:57:05
# @Runtime: 45 ms
# @Memory: N/A

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        imax, imin = 1, 1
        ans = nums[0]
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax = max(num, imax * num)
            imin = min(num, imin * num)
            ans = max(ans, imax)
        return ans
            
        
        
