
# @Title: 两数相除 (Divide Two Integers)
# @Author: cocofe
# @Date: 2020-02-11 01:06:05
# @Runtime: 12 ms
# @Memory: N/A

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if (dividend <= 0 and divisor < 0) or (dividend >= 0 and divisor > 0):
            sign = 1
        else:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        overflows = [-2 ** 31, 2**31 - 1]
        quotient = 0
        divisor_sum = 0
        quotient_sum = 0
        if divisor == 1:
            quotient = sign * dividend
        else:
            while dividend >= divisor: 
                divisor_sum = divisor
                sub_count = 1
                dividend -= divisor
                quotient += 1
                while dividend >= divisor and divisor_sum + divisor_sum <= dividend:
                    divisor_sum += divisor_sum
                    dividend -= divisor_sum
                    sub_count += sub_count
                    quotient += sub_count
            quotient = sign * quotient
        if overflows[0] <= quotient <= overflows[1]:
            return quotient
        return overflows[1]
            
        
        
        
        
