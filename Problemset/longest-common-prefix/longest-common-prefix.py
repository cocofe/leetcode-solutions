
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: cocofe
# @Date: 2020-01-08 13:10:58
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for s in strs:
            if not s:
                return ""
        ret = ''
        length = min(map(len, strs))
        for i in range(0, length):
            tmp = ''
            is_same = True
            for s in strs:
                if tmp:
                    if s[i] != tmp:
                        is_same = False
                else:
                    tmp = s[i]
            if is_same:
                ret += tmp
            else:
                break
        return ret
            
