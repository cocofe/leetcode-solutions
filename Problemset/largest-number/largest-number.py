
# @Title: 最大数 (Largest Number)
# @Author: cocofe
# @Date: 2021-04-12 01:06:29
# @Runtime: 44 ms
# @Memory: 15.1 MB

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(x + y) - int(y + x)
        nums = map(str, nums)
        nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
        left = 0
        while left < len(nums):
            if int(nums[left]) == 0:
                left += 1
            else:
                break
        return ''.join(nums[left:]) or '0'
        
