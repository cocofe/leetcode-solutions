
# @Title: 摆动序列 (Wiggle Subsequence)
# @Author: cocofe
# @Date: 2021-04-23 02:47:38
# @Runtime: 24 ms
# @Memory: 13 MB

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h, l = 1, 1
        for i in range(1, len(nums)):
            num = nums[i]
            prev = nums[i-1]
            if num > prev:
                h = max(h, l + 1)
            elif num < prev:
                l = max(l, h + 1)
        return max([h, l])
