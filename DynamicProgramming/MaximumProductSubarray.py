# -*- coding: UTF-8 -*-
from collections import defaultdict


class Solution(object):
    """
    Find the contiguous subarray within an array (containing at least one number) which has the largest product.

    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.
    """
    def maxProduct(self, nums):
        """
        目的是求最大的子数组连续乘积的值, 可以找到如下规律
         - 当前元素的最大值为以当前元素为结尾的子数组连续乘积, 或者是当前元素
         - 最后元素的最大值不代表是全局的最大值,
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

    def test(self):
        nums = [-3,-2,-4]
        print self.maxProduct(nums)


