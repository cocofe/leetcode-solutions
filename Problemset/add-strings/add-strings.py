
# @Title: 字符串相加 (Add Strings)
# @Author: cocofe
# @Date: 2021-04-06 23:09:56
# @Runtime: 44 ms
# @Memory: 15 MB

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        add = 0
        n1, n2 = len(num1) - 1, len(num2) - 1
        idx = 0
        ans = []
        while n1 >= 0 and n2 >= 0:
            val = int(num1[n1]) + int(num2[n2]) + add
            ans.append(str(val % 10))
            add = val // 10
            n1 -= 1
            n2 -= 1
        while n1 >= 0:
            val = int(num1[n1]) + add
            ans.append(str(val % 10))
            add = val // 10
            n1 -= 1
        while n2 >= 0:
            val = int(num2[n2]) + add
            ans.append(str(val % 10))
            add = val // 10
            n2 -= 1
        if add:
            ans.append(str(add))
        return ''.join(ans[::-1])

