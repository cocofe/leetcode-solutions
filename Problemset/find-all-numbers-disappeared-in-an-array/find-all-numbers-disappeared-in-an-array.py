
# @Title: 找到所有数组中消失的数字 (Find All Numbers Disappeared in an Array)
# @Author: cocofe
# @Date: 2020-04-01 00:08:27
# @Runtime: 348 ms
# @Memory: N/A

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = 0 - abs(nums[idx])
        return [idx+1 for idx, num in enumerate(nums) if num > 0]
            
        
