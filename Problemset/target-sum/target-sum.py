
# @Title: 目标和 (Target Sum)
# @Author: cocofe
# @Date: 2020-11-09 21:48:09
# @Runtime: 176 ms
# @Memory: 13.1 MB

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        for num in nums:
            if not dp:
                dp[num] += 1
                dp[0-num] += 1
            else:
                tmp = collections.defaultdict(int)
                for _sum, _count in dp.items():
                    tmp[_sum + num] += _count
                    tmp[_sum - num] += _count
                dp = tmp
        return dp[S]
            
