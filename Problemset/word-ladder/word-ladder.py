
# @Title: 单词接龙 (Word Ladder)
# @Author: cocofe
# @Date: 2020-11-06 00:43:33
# @Runtime: 2224 ms
# @Memory: 13.7 MB

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def is_valid(s, e):
            _unique_count = 0
            for _s, _e in zip(s, e):
                if _s != _e:
                    _unique_count += 1
                if _unique_count > 1:
                    break
            return _unique_count == 1
        if endWord not in wordList: return 0
        q1 = set()
        q2 = set()
        q1.add(beginWord)
        q2.add(endWord)
        step = 1
        visited = set([beginWord, endWord])
        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            tmp = set()
            for nex in q1:
                for word in wordList:
                    if is_valid(nex, word):
                        if word in q2:
                            return step + 1
                        if word not in visited:
                            tmp.add(word)
                            visited.add(word)
            step += 1
            q1 = tmp
        return 0
