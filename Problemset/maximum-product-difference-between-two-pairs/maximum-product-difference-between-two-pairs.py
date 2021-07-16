
# @Title: 两个数对之间的最大乘积差 (Maximum Product Difference Between Two Pairs)
# @Author: cocofe
# @Date: 2021-06-27 10:39:12
# @Runtime: 56 ms
# @Memory: 15.6 MB

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # a,b = nums[-1], nums[-2]
        return abs(nums[-1] * nums[-2] - nums[0] * nums[1]) 
