
# @Title: 多数元素 (Majority Element)
# @Author: cocofe
# @Date: 2020-04-01 23:43:15
# @Runtime: 172 ms
# @Memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        ans = Counter(nums)
        for key, count in ans.items():
            if count >= len(nums) / 2.0:
                return key
        
        
