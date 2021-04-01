
# @Title: 翻转图像 (Flipping an Image)
# @Author: cocofe
# @Date: 2021-02-24 02:11:05
# @Runtime: 28 ms
# @Memory: 13.1 MB

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for idx, a in enumerate(A):
            A[idx] = a[::-1]
        for a in A:
            for idx, num in enumerate(a):
                a[idx] ^= 1
        return A 
            
