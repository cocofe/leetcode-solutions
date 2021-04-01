
# @Title: 连续子数组的最大和 (连续子数组的最大和  LCOF)
# @Author: cocofe
# @Date: 2020-12-11 22:22:29
# @Runtime: 52 ms
# @Memory: 15 MB

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('-inf')
        prev = 0
        for num in nums:
            curr = max(num, num+prev)
            ans = max(ans, curr)
            prev = curr
        return ans
