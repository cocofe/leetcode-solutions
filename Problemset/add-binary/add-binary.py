
# @Title: 二进制求和 (Add Binary)
# @Author: cocofe
# @Date: 2020-03-17 21:59:52
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        length = max(len_a, len_b)
        idx = 0
        carry = 0
        ans = []
        while idx < length:
            i = -1 - idx
            if idx < len_a:
                _a = int(a[i])
            else:
                _a = 0
            if idx < len_b:
                _b = int(b[i])
            else:
                _b = 0
            remain = (_a + _b + carry) % 2
            carry = (_a + _b + carry) // 2
            ans.append(remain)
            idx += 1
        if carry:
            ans.append(carry)
        ans = map(str, ans)
        ans.reverse()
        return ''.join(ans)
        
            
        
