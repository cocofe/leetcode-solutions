# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Note: This is an extension of House Robber.

    After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
    
    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


    """
    def rob(self, nums):
        """
        数组变成环形数组, 刚开始没有想到好的方法, 看了网上的解析后, 才懂了,,,
        环形数组与正常数组唯一区别就是, 首尾只能选其一, 如果都不选肯定值不是最大的
        因此可以分别判断分别去掉首和尾的情况, 这时数组即可当做正常数组对待
        :type nums: List[int]
        :rtype: int
        """
        fir, sec, fir2, sec2 = 0, 0, 0, 0
        for idx, val in enumerate(nums):
            if idx == 0:
                fir, sec = max(fir, sec+val), fir
            elif idx == len(nums) - 1:
                fir2, sec2 = max(fir2, sec2+val), fir2
            else:
                fir, sec = max(fir, sec+val), fir
                fir2, sec2 = max(fir2, sec2+val), fir2
        return max(fir,fir2,sec,sec2)



