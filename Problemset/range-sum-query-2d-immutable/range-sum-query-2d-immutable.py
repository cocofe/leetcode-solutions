
# @Title: 二维区域和检索 - 矩阵不可变 (Range Sum Query 2D - Immutable)
# @Author: cocofe
# @Date: 2021-03-02 03:06:19
# @Runtime: 304 ms
# @Memory: 15.7 MB

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self._sum = []
        for row in matrix:
            prev = 0
            col_sum = []
            for col in row:
                s = prev + col
                col_sum.append(s)
                prev = s
            self._sum.append(col_sum)

    def get_sum(self, row, col_1, col_2):
        return self._sum[row][col_2] - (self._sum[row][col_1 - 1] if col_1 - 1 >= 0 else 0)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for row in range(row1, row2+1):
            ans += self.get_sum(row, col1, col2)
        return ans




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
