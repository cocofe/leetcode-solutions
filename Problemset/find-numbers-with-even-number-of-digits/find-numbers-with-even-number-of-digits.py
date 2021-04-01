
# @Title: 统计位数为偶数的数字 (Find Numbers with Even Number of Digits)
# @Author: cocofe
# @Date: 2020-01-26 17:41:17
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ret += 1
                
        return ret
