
# @Title: 最长回文子串 (Longest Palindromic Substring)
# @Author: cocofe
# @Date: 2018-04-13 10:47:25
# @Runtime: 1246 ms
# @Memory: N/A

class Solution(object):
    def helper(self, left, right, s, ans):
        if left < 0 or right >= len(s) or left > right:
            return
        # print 'check {}~{}: {}'.format(left, right, s[left:right+1])
        
        if s[left] != s[right]:
            self.helper(left-1, right, s, ans)
            self.helper(left, right+1, s, ans)
            return
        if right - left + 1 > len(ans[0]):
            ans[0] = s[left:right+1]
        if left == right:
            self.helper(left-1, right, s, ans)
            self.helper(left, right+1, s, ans)
        return self.helper(left-1, right+1, s, ans)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = (len(s) - 1) / 2
        if len(s) % 2 == 0:
            right = left + 1
        else:
            right = left
        ans = ['']
        self.helper(left, right, s, ans)
        return ans[0] or s[0] if s else ''
        
