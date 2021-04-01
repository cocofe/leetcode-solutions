
# @Title: 正则表达式匹配 (Regular Expression Matching)
# @Author: cocofe
# @Date: 2020-11-27 01:26:43
# @Runtime: 68 ms
# @Memory: 13.2 MB

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = []
        wild_map = []
        p_idx = 0
        while p_idx < len(p):
            _p = p[p_idx]
            if _p == '*':
                p_idx += 1
                continue
            is_wild_char = bool(p_idx + 1 < len(p) and p[p_idx + 1] == '*')
            pattern.append(_p)
            wild_map.append(is_wild_char)
            p_idx += 1

        def is_match(_s, _p):
            return _p == '.' or _s == _p

        def dp(i, j):
            if j < 0:
                return i < 0
            is_wild_char = wild_map[j]
            if is_wild_char:
                if i >= 0 and is_match(s[i], pattern[j]):
                    return dp(i, j-1) or dp(i-1, j)
                return dp(i, j-1)
            else:
                if i >= 0 and is_match(s[i], pattern[j]):
                    return dp(i-1, j-1)
            return False
        return dp(len(s)-1, len(pattern)-1)
        



        

