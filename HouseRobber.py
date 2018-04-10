# -*- coding: UTF-8 -*-
class Solution(object):
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


    """
    def rob(self, nums):
        """
        一个非负数组, 不能连续取相邻的数,求取得数最大值
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * length
        if not nums:
            return 0
        elif length == 1:
            return nums[0]
        for idx, val in enumerate(nums):
            if idx == 0 or idx == 1:
                dp[idx] = val
            elif idx == 2:
                dp[idx] = val + dp[idx - 2]
            else:
                dp[idx] = max(dp[idx - 2], dp[idx - 3]) + val
        return max(dp[length - 1], dp[length - 2])

    def rob2(self, nums):
        """
        第二种方法, 更简单, 对于每个元素,只有取或者不取, 如果不取,则结果等同于上一个元素的值(fir), 
        如果取,则结果为(sec+val) val为当前元素的值, 比较取或者不取两种结果的大小,取最大值
        :type nums: List[int]
        :rtype: int
        """
        fir, sec = 0, 0
        for idx, val in enumerate(nums):
            sec, fir = fir, max(fir, sec + val)
        return max(fir, sec)
