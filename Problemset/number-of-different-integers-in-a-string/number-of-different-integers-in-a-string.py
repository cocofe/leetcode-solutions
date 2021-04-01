
# @Title: 字符串中不同整数的数目 (Number of Different Integers in a String)
# @Author: cocofe
# @Date: 2021-03-28 11:11:33
# @Runtime: 32 ms
# @Memory: 13.1 MB

class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        string = []
        for w in word:
            if not w.isdigit():
                string.append(' ')
            else:
                string.append(w)
        s = ''.join(string)
        return len(set(map(int, s.split())))
