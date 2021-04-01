
# @Title: 独一无二的出现次数 (Unique Number of Occurrences)
# @Author: cocofe
# @Date: 2020-10-28 21:24:32
# @Runtime: 20 ms
# @Memory: 13.2 MB

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dp = collections.defaultdict(int)
        for num in arr:
            dp[num] += 1
        return len(dp.values()) == len(set(dp.values()))
