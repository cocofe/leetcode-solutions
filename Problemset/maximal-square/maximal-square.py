
# @Title: 最大正方形 (Maximal Square)
# @Author: cocofe
# @Date: 2021-04-05 09:13:53
# @Runtime: 92 ms
# @Memory: 20.7 MB

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    ans = max(ans, dp[i][j])
        return ans * ans

