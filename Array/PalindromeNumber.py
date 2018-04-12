# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Determine whether an integer is a palindrome. Do this without extra space.
    """
    def isPalindrome(self, x):
        """
        思路是将x 一分为二, 判断两边是否相同, 看了别人的代码后,发现更好的解决方法是将x翻转, 直接判断是否相同
        :type x: int
        :rtype: bool
        """
        if x // 10 == 0:
            return True
        elif x < 0:
            return False
        y = 0
        index = 0
        while x > y:
            y = y * 10 + x % 10
            x = x // 10
            index += 1
        index -= 1
        if x == y and y // 10 ** index != 0:
            return True
        elif y // 10 ** index != 0 and x // 10 ** index == 0 and y // 10 == x:
            return True
        else:
            return False

    def isPalindrome2(self, x):
        if x < 0:
            return False
        y = 0
        tmp_x = x
        while tmp_x > 0:
            y = y * 10 + tmp_x % 10
            tmp_x = tmp_x // 10
        return x == y

    def test(self):
        x = 21120
        print self.isPalindrome(x)





