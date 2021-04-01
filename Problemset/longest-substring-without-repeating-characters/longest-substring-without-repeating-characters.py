
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: cocofe
# @Date: 2018-04-03 15:27:13
# @Runtime: 88 ms
# @Memory: N/A

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        start = max_length = 0
        for idx, val in enumerate(s):
            if val in used and start <= used[val]:
                start = used[val] + 1  # update start index
            else:
                max_length = max(max_length, idx - start + 1)
            used[val] = idx
        return max_length
        
                
                
                
        
