
# @Title: 和为s的连续正数序列 (和为s的连续正数序列 LCOF)
# @Author: cocofe
# @Date: 2020-03-06 01:42:51
# @Runtime: 428 ms
# @Memory: 14 MB

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        if target < 3:
            return []
        ret = []
        for i in range(1, target):
            total_sum = 0
            result = []
            begin = i
            while total_sum < target:
                result.append(begin)
                total_sum += begin
                begin += 1
            if total_sum == target:
                ret.append(result)
        return ret
            


