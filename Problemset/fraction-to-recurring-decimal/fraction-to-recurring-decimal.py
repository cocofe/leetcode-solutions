
# @Title: 分数到小数 (Fraction to Recurring Decimal)
# @Author: cocofe
# @Date: 2020-03-05 01:09:44
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator * denominator < 0:
            sign = -1
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            sign = 1
        if sign == -1:
            ret = '-'
        else:
            ret = ''
        ret += str(numerator // denominator)
        left_num = numerator % denominator
        if left_num == 0:
            return ret
        ret += '.'
        nums = []
        while True:
            left_num *= 10
            quotient = left_num // denominator
            remainder = left_num % denominator
            tmp = (str(quotient), str(remainder))
            if tmp in nums:
                idx = nums.index(tmp)
                for i in range(0, idx):
                    ret += nums[i][0]
                dup_str = ''
                for i in range(idx, len(nums)):
                    dup_str += nums[i][0]
                ret += '(%s)' % dup_str
                return ret
            else:
                nums.append(tmp)
            if remainder == 0:
                break
            left_num = remainder
        if nums:
            for string, _ in nums:
                ret += string
        return ret
