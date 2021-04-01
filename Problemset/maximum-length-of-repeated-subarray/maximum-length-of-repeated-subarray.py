
# @Title: 最长重复子数组 (Maximum Length of Repeated Subarray)
# @Author: cocofe
# @Date: 2020-12-16 02:09:37
# @Runtime: 3328 ms
# @Memory: 90.9 MB

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        ans = 0
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                if a == b:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(dp[i][j], ans)
        return ans
