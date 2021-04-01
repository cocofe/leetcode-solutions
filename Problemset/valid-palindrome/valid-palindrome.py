
# @Title: 验证回文串 (Valid Palindrome)
# @Author: cocofe
# @Date: 2021-02-14 23:50:47
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        left, right = 0, len(s) - 1
        while left < right:
            if not (s[left].isdigit() or s[left].isalpha()):
                left += 1
                continue
            elif not (s[right].isdigit() or s[right].isalpha()):
                right -= 1
                continue
            else:
                # print 'check {}:{}  {}:{}'.format(left, s[left], right, s[right])
                if s[left].lower() != s[right].lower():
                    return False
            left += 1
            right -= 1
        return True

