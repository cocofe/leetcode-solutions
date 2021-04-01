
# @Title: 反转字符串 (Reverse String)
# @Author: cocofe
# @Date: 2020-08-16 20:38:30
# @Runtime: 36 ms
# @Memory: 18.8 MB

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        bp, ep = 0, len(s) - 1
        while bp < ep:
            s[bp], s[ep] = s[ep], s[bp]
            bp += 1
            ep -= 1
        
