
# @Title: 6 和 9 组成的最大数字 (Maximum 69 Number)
# @Author: cocofe
# @Date: 2020-01-26 19:26:04
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        index = None
        for idx, dig in enumerate(string):
            if dig == '6':
                index = idx
                break
        dig_set = [s for s in string]
        if index is not None:
            dig_set[index] = '9'
        return int(''.join(dig_set))
        
