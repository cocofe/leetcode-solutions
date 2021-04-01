
# @Title: 只出现一次的数字 (Single Number)
# @Author: cocofe
# @Date: 2020-04-01 21:53:41
# @Runtime: 60 ms
# @Memory: N/A

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            ans ^= n
        return ans
            
            
        
        
        
