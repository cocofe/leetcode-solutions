
# @Title: 统计全为 1 的正方形子矩阵 (Count Square Submatrices with All Ones)
# @Author: cocofe
# @Date: 2020-01-10 22:22:47
# @Runtime: 716 ms
# @Memory: N/A

from collections import defaultdict


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = defaultdict(dict)
        width = len(matrix[0])
        high = len(matrix)
        for i in range(0, high):
            for j in range(0, width):
                val = matrix[i][j]
                if i - 1 < 0 or j - 1 < 0:
                    dp[i][j] = val
                else:
                    if val == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        count = 0
        for i in range(0, high):
            for j in range(0, width):
                count += dp[i][j]
        return count
