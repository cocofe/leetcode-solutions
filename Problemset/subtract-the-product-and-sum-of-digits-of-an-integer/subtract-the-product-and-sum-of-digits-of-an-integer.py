
# @Title: 整数的各位积和之差 (Subtract the Product and Sum of Digits of an Integer)
# @Author: cocofe
# @Date: 2020-01-26 17:44:01
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        _sum = 0
        for s in str(n):
            prod *= int(s)
            _sum += int(s)
        return prod - _sum
            
        
