
# @Title: 整数转罗马数字 (Integer to Roman)
# @Author: cocofe
# @Date: 2020-07-10 00:15:26
# @Runtime: 64 ms
# @Memory: N/A

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_map = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: "CD",
            900: "CM",
        }
        ans = []
        for i in (1000, 100, 10, 1):
            val = num // i
            left = num % i
            if val == 0:
                continue
            if val * i not in num_map:
                if val > 5:
                    ans.append(num_map[i * 5] + num_map[i] * (val - 5))
                else:
                    ans.append(num_map[i] * val)
            else:
                ans.append(num_map[val * i])
            num = left
        return ''.join(ans)


        

