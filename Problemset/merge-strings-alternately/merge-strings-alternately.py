
# @Title: 交替合并字符串 (Merge Strings Alternately)
# @Author: cocofe
# @Date: 2021-02-21 10:33:31
# @Runtime: 24 ms
# @Memory: 12.9 MB

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lp, rp = 0, 0
        ans = []
        while lp < len(word1) and rp < len(word2):
            ans.append(word1[lp])
            ans.append(word2[rp])
            lp += 1
            rp += 1
        while lp < len(word1):
            ans.append(word1[lp])
            lp += 1
        while rp < len(word2):
            ans.append(word2[rp])
            rp += 1
        return ''.join(ans)
            
