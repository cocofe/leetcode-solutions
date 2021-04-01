
# @Title: 单词规律 (Word Pattern)
# @Author: cocofe
# @Date: 2020-04-10 11:17:23
# @Runtime: 16 ms
# @Memory: N/A

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        p_map = {}
        if len(str) != len(pattern):
            return False
        return all([str[idx] == str[pattern.index(p)] and p == pattern[pattern.index(p)] for idx, p in enumerate(pattern)])
            
            
        
