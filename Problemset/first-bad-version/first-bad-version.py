
# @Title: 第一个错误的版本 (First Bad Version)
# @Author: cocofe
# @Date: 2021-03-03 00:06:38
# @Runtime: 20 ms
# @Memory: 12.9 MB

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if isBadVersion(mid+1):
                right = mid - 1
            else:
                left = mid + 1
        return left + 1
