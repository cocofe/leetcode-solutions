
# @Title: 矩阵置零 (Set Matrix Zeroes)
# @Author: cocofe
# @Date: 2021-03-21 00:25:06
# @Runtime: 36 ms
# @Memory: 13.7 MB

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        columns = set()
        rows = set()
        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if col == 0:
                    columns.add(col_idx)
                    rows.add(row_idx)
        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if row_idx in rows or col_idx in columns:
                    matrix[row_idx][col_idx] = 0
        
                
