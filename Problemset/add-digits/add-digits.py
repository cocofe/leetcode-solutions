
# @Title: 各位相加 (Add Digits)
# @Author: cocofe
# @Date: 2020-04-01 23:37:31
# @Runtime: 16 ms
# @Memory: N/A

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return num
        return num % 9 or 9
        
