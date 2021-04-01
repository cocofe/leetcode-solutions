
# @Title: 最大升序子数组和 (Maximum Ascending Subarray Sum)
# @Author: cocofe
# @Date: 2021-03-21 10:51:52
# @Runtime: 16 ms
# @Memory: 12.9 MB

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curr = 0
        prev = float('-inf')
        for num in nums:
            if num <= prev:
                prev = num
                curr = num
            else:
                curr += num
                prev = num
            ans = max(ans, curr)
        return ans
