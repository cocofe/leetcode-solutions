
# @Title: 单词拆分 (Word Break)
# @Author: cocofe
# @Date: 2020-01-09 23:22:18
# @Runtime: 32 ms
# @Memory: N/A

from collections import defaultdict

class Solution(object):

    def _wordBreak(self, s, wordDict, begin, end, dp):
        tmp = ''
        if begin >= end:
            return True
        if begin in dp and end in dp[begin]:
            return dp[begin][end]
        ret = []
        for i in range(begin, end):
            tmp += s[i]
            if tmp in wordDict:
                ret.append(self._wordBreak(s, wordDict, i + 1, end, dp))
        dp[begin][end] = any(ret)
        return dp[begin][end]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        ret = []
        tmp = ''
        dp = defaultdict(dict)
        for i in range(0, length):
            tmp += s[i]
            if tmp in wordDict:
                ret.append(self._wordBreak(s, wordDict, i + 1, length, dp))
        return any(ret)
