
# @Title: 转置矩阵 (Transpose Matrix)
# @Author: cocofe
# @Date: 2021-02-25 22:16:43
# @Runtime: 28 ms
# @Memory: 13.8 MB

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(A)
        ans = []
        for i in range(len(A[0])):
            x = []
            for j in range(length):
                x.append(A[j][i])
            ans.append(x)
        return ans
