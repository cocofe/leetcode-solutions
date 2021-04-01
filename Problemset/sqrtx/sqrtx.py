
# @Title: x 的平方根 (Sqrt(x))
# @Author: cocofe
# @Date: 2020-08-13 01:16:01
# @Runtime: 36 ms
# @Memory: 12.3 MB

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        begin = 0
        end = x
        mid = 0
        while begin <= end:
            mid = (begin + end) / 2
            assume = mid ** 2
            if assume <= x and int(assume - x) == 0:
                break
            elif assume > x:
                end = int(mid) - 1
            else:
                begin = int(mid) + 1
        return mid if mid ** 2 <= x else mid - 1
