
# @Title: 构成特定和需要添加的最少元素 (Minimum Elements to Add to Form a Given Sum)
# @Author: cocofe
# @Date: 2021-03-07 10:54:33
# @Runtime: 56 ms
# @Memory: 19.7 MB

class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        left = abs(goal - sum(nums))
        plus = 1 if left % limit != 0 else 0
        return left // limit + plus
