
# @Title: 旋转图像 (Rotate Image)
# @Author: cocofe
# @Date: 2021-04-04 23:45:09
# @Runtime: 36 ms
# @Memory: 15 MB

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        # 0,1
        # 1,2
        # 2,1
        # 1,0
        n = len(matrix)
        for row in range(n // 2):
            # 长度为4, 遍历0,1
            # 长度为3, 遍历0,1
            for col in range((n+1) // 2):
                # 对于矩阵中第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置
                tmp = matrix[row][col]
                # print((n-col-1, row), (row, col), (col, n-row-1), (n-row-1, n-col-1))
                matrix[row][col] = matrix[n-col-1][row]
                matrix[n-col-1][row] = matrix[n-row-1][n-col-1]
                matrix[n-row-1][n-col-1] = matrix[col][n - row - 1]
                matrix[col][n - row - 1] = tmp
                




