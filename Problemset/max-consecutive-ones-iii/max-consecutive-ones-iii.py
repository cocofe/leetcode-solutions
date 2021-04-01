
# @Title: 最大连续1的个数 III (Max Consecutive Ones III)
# @Author: cocofe
# @Date: 2021-02-19 16:29:35
# @Runtime: 576 ms
# @Memory: 13.3 MB

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left, right = 0, 0
        zero_size = 0
        ans = 0
        while right < len(A):
            if A[right] == 0:
                zero_size += 1
            while zero_size > K and left <= right:
                if A[left] == 0:
                    zero_size -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return max(ans, right - left)
        
