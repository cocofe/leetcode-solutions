
# @Title: 01 矩阵 (01 Matrix)
# @Author: cocofe
# @Date: 2020-03-17 01:47:07
# @Runtime: 532 ms
# @Memory: N/A

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        max_num = len(matrix) * len(matrix[0])
        dp = []
        for r in range(len(matrix)):
            col = []
            for c in range(len(matrix[0])):
                col.append(max_num)
            dp.append(col)
        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                if col == 0:
                    dp[r][c] = 0
                else:
                    up = dp[r-1][c] if r - 1 > -1 else max_num
                    left = dp[r][c-1] if c - 1 > -1 else max_num
                    dp[r][c] = min(up, left) + 1
        for r in range(len(matrix)-1, -1, -1):
            for c in range(len(matrix[0])-1, -1, -1):
                if matrix[r][c] == 1:
                    rigth = dp[r][c+1] if c + 1 < len(row) else max_num
                    down = dp[r+1][c] if r + 1 < len(matrix) else max_num
                    dp[r][c] = min(min(down, rigth) + 1, dp[r][c])
                
        return dp
        
                    
                    
                    
                
                
        
