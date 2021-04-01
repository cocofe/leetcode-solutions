
# @Title: 不同路径 II (Unique Paths II)
# @Author: cocofe
# @Date: 2018-04-09 16:23:15
# @Runtime: 34 ms
# @Memory: N/A

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        width = len(obstacleGrid[0])
        d = [0] * width
        d[0] = 1
        for _, row in enumerate(obstacleGrid):
            for col_idx, col_val in enumerate(row):
                if col_val == 1:
                    # 通过该点的路的条数为0
                    d[col_idx] = 0
                else:
                    # 该点的路的条数 = top + left
                    if col_idx - 1 >= 0:
                        d[col_idx] += d[col_idx - 1]
        return d[width-1]
                
        
