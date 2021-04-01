
# @Title: 调整数组顺序使奇数位于偶数前面 (调整数组顺序使奇数位于偶数前面 LCOF)
# @Author: cocofe
# @Date: 2021-03-08 22:19:43
# @Runtime: 44 ms
# @Memory: 18.8 MB

class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a,b = [],[]
        for num in nums:
            if num % 2 == 0:
                b.append(num)
            else:
                a.append(num)
        return a + b
