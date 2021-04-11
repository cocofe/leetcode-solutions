
# @Title: 丢失的数字 (Missing Number)
# @Author: cocofe
# @Date: 2021-04-11 15:05:17
# @Runtime: 40 ms
# @Memory: 15.8 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = [False] * (len(nums) + 1)
        for num in nums:
            n[num] = True
        for idx, bl in enumerate(n):
            if not bl:
                return idx
            
