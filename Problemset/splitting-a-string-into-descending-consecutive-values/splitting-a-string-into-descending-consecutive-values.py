
# @Title: 将字符串拆分为递减的连续值 (Splitting a String Into Descending Consecutive Values)
# @Author: cocofe
# @Date: 2021-05-02 11:11:10
# @Runtime: 56 ms
# @Memory: 15 MB

class Solution:
    def splitString(self, s: str) -> bool:
        cache = {}
        def backtrack(idx, target):
            if idx >= len(s):
                return True
            if (idx, target) in cache:
                return cache[(idx, target)]
            ans = False
            for i in range(idx, len(s)):
                if int(s[idx:i+1]) == target:
                    ans = backtrack(i+1, int(s[idx:i+1]) - 1) or ans
            cache[(idx, target)] = ans
            return ans
        for i in range(0, len(s) - 1):
            if backtrack(i+1, int(s[:i+1]) - 1):
                return True
        return False
