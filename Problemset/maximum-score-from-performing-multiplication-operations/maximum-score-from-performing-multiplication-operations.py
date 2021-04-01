
# @Title: 执行乘法运算的最大分数 (Maximum Score from Performing Multiplication Operations)
# @Author: cocofe
# @Date: 2021-02-23 22:40:59
# @Runtime: 9556 ms
# @Memory: 157.3 MB

from functools import lru_cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(None)
        def backtrace(left, right, i):
            if i == len(multipliers):
                return 0
            return max(nums[left] * multipliers[i] + backtrace(left+1, right, i+1),
                       nums[right] * multipliers[i] + backtrace(left, right-1, i+1))
        res = backtrace(0, len(nums)-1, 0)
        backtrace.cache_clear()
        return res
