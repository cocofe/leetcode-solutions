# -*- coding: UTF-8 -*-
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        idx, sign = 0, '+'
        INT_MAX, INT_MIN = 2 ** 31 - 1, - 2 ** 31
        # ignore whitespace
        while idx < len(str):
            if str[idx] == ' ':
                idx += 1
                continue
            break
        if idx >= len(str):
            return 0
        if not ('0' <= str[idx] <= '9' or str[idx] in ('-', '+')):
            return 0
        if str[idx] in ('-', '+'):
            sign = str[idx]
            idx += 1
        num = 0
        while idx < len(str):
            if '0' <= str[idx] <= '9':
                num = num * 10 + int(str[idx])
                if sign == '+' and num >= INT_MAX:
                    return INT_MAX
                elif sign == '-' and num >= abs(INT_MIN):
                    return INT_MIN
                idx += 1
                continue
            break
        return num if sign == '+' else 0 - num





