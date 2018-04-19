# -*- coding: UTF-8 -*-
from collections import defaultdict


class NumArray(object):
    def __init__(self, nums):
        """
        Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

        Example:
        Given nums = [-2, 0, 3, -5, 2, -1]
        
            sumRange(0, 2) -> 1
            sumRange(2, 5) -> -1
            sumRange(0, 5) -> -3
        Note:
        
        You may assume that the array does not change.
        There are many calls to sumRange function.

        Your NumArray object will be instantiated and called as such:
        obj = NumArray(nums)
        param_1 = obj.sumRange(i,j)
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = defaultdict(lambda: defaultdict(int))
        self.d = nums
        for idx, val in enumerate(nums):
            self.d[idx] = self.d[idx-1] + val if idx >=1 else val

    def sumRange_TLE(self, i, j):
        """
        利用dp数组记忆计算结果, 会Time Limit Exceeded
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.dp[i][j]:
            return self.dp[i][j]
        for x in range(i, j + 1):
            if self.dp[i][x]:
                continue
            self.dp[i][x] = self.dp[i][x - 1] + self.nums[x]
        return self.dp[i][j]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.d[j] - (self.d[i - 1] if i >= 1 else 0)



    @staticmethod
    def test():
        nums = [-2, 0, 3, -5, 2, -1]
        obj = NumArray(nums)
        param_1 = obj.sumRange(0,4)
        print param_1