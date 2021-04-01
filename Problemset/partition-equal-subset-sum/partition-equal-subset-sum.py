
# @Title: 分割等和子集 (Partition Equal Subset Sum)
# @Author: cocofe
# @Date: 2020-10-22 22:47:07
# @Runtime: 1256 ms
# @Memory: 13.6 MB

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return True
        dp = collections.defaultdict(set)
        prev_sum = 0
        prev, curr = set(), set()
        for i, n in enumerate(nums):
            # prev = dp[i-1]
            if i == len(nums) - 1:
                return n in prev
            for _p in prev:
                curr.add(abs(_p + n))
                curr.add(abs(_p - n))
            curr.add(abs(prev_sum - n))
            prev_sum += n
            prev = curr
            curr = set()
        return False
