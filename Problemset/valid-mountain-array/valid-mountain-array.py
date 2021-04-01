
# @Title: 有效的山脉数组 (Valid Mountain Array)
# @Author: cocofe
# @Date: 2020-11-03 21:38:17
# @Runtime: 172 ms
# @Memory: 14.3 MB

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        i = 1
        while i < length and A[i-1] < A[i]:
            i += 1
        i -= 1
        if i == 0 or i == length - 1:
            return False
        i += 1
        while i < length and A[i-1] > A[i]:
            i += 1
        return i == length
        
