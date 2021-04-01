
# @Title: 回文数 (Palindrome Number)
# @Author: cocofe
# @Date: 2018-04-09 13:21:01
# @Runtime: 340 ms
# @Memory: N/A

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = 0
        tmp_x = x
        while tmp_x > 0:
            y = y * 10 + tmp_x % 10
            tmp_x = tmp_x // 10
        return x == y
        
        
