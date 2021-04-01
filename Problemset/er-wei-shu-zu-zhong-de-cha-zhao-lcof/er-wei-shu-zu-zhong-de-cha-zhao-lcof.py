
# @Title: 二维数组中的查找 (二维数组中的查找 LCOF)
# @Author: cocofe
# @Date: 2020-03-06 01:49:45
# @Runtime: 28 ms
# @Memory: 15.3 MB

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if not row:
                return False
            if row[0] > target:
                return False
            elif row[0] == target:
                return True
            for col in row:
                if col < target:
                    continue
                elif col == target:
                    return True
                else:
                    break
        return False
