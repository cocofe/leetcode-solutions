
# @Title: 加一 (Plus One)
# @Author: cocofe
# @Date: 2020-07-09 21:09:08
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = -1
        digits[idx] += 1
        carry = 0
        while abs(idx) <= len(digits):
            digits[idx] += carry
            carry = digits[idx] // 10
            left = digits[idx] % 10
            if carry == 0:
                break
            digits[idx] = left
            idx -= 1
        if carry:
            digits = [carry] + digits
        return digits
        

