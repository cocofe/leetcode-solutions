
# @Title: 最大子序和 (Maximum Subarray)
# @Author: cocofe
# @Date: 2019-10-16 01:13:24
# @Runtime: 52 ms
# @Memory: N/A

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for idx, val in enumerate(nums):
            if idx == 0:
                dp.append(val)
            else:
                old = max(dp[-1], 0)
                dp.append(max(old + val, val))
        return max(dp)
            
        
            
                
                
