
# @Title: 数组中重复的数字 (数组中重复的数字 LCOF)
# @Author: cocofe
# @Date: 2020-03-06 01:45:37
# @Runtime: 36 ms
# @Memory: 18 MB

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_s = set()
        for n in nums:
            if n in n_s:
                return n
            n_s.add(n)
