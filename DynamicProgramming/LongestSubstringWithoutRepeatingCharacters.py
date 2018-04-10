# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Examples:
    
    Given "abcabcbb", the answer is "abc", which the length is 3.
    
    Given "bbbbb", the answer is "b", with the length of 1.
    
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

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




