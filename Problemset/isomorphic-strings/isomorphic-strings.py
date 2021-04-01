
# @Title: 同构字符串 (Isomorphic Strings)
# @Author: cocofe
# @Date: 2020-12-27 15:01:29
# @Runtime: 28 ms
# @Memory: 15.9 MB

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        for i, j in zip(s, t):
            if i in mapping and mapping[i] != j:
                return False
            if i == j:
                if i not in mapping and j in mapping.values():
                    return False
                mapping[i] = j
                continue
            if mapping.get(i) is not None:
                if mapping[i] == j:
                    continue
                return False
            if j in mapping.values():
                return False
            mapping[i] = j
        return True
