
# @Title: 第一个错误的版本 (First Bad Version)
# @Author: cocofe
# @Date: 2021-06-13 12:37:53
# @Runtime: 36 ms
# @Memory: 14.8 MB

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
urn left + 1
