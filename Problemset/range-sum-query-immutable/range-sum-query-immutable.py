
# @Title: 区域和检索 - 数组不可变 (Range Sum Query - Immutable)
# @Author: cocofe
# @Date: 2021-03-01 19:30:41
# @Runtime: 184 ms
# @Memory: 16.8 MB

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._sum = []
        prev = 0
        for i, num in enumerate(nums):
            self._sum.append(prev + num)
            prev += num

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self._sum[j]
        return self._sum[j] - self._sum[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
