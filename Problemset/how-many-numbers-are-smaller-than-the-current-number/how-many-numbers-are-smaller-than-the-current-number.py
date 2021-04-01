
# @Title: 有多少小于当前数字的数字 (How Many Numbers Are Smaller Than the Current Number)
# @Author: cocofe
# @Date: 2020-10-26 23:29:56
# @Runtime: 16 ms
# @Memory: 13.2 MB

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = nums
        nums = sorted(nums)
        dp = {}
        for idx, num in enumerate(nums):
            if num in dp:
                continue
            dp[num] = idx
        return [dp[num] for num in tmp]
