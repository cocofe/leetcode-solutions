
# @Title: 最长不含重复字符的子字符串 (最长不含重复字符的子字符串 LCOF)
# @Author: cocofe
# @Date: 2020-12-16 02:23:18
# @Runtime: 60 ms
# @Memory: 13.4 MB

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        left, right = 0, 1
        windows = {s[0]}
        ans = 0
        while right < len(s):
            if s[right] not in windows:
                windows.add(s[right])
            else:
                ans = max(ans, len(windows))
                while left <= right:
                    _s = s[left]
                    left += 1
                    if _s == s[right]:
                        break
                    windows.remove(_s)                    
            right += 1
        return max(ans, len(windows))
                

        
