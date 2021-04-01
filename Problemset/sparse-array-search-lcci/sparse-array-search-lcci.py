
# @Title: 稀疏数组搜索 (Sparse Array Search LCCI)
# @Author: cocofe
# @Date: 2021-03-02 03:25:26
# @Runtime: 16 ms
# @Memory: 13.1 MB

class Solution(object):
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        idxs, filter_words = [], []
        for idx, word in enumerate(words):
            if word == "":
               continue
            idxs.append(idx)
            filter_words.append(word)
        left, right = 0, len(filter_words) - 1
        while left <= right:
            mid = (left + right) / 2
            if filter_words[mid] == s:
                return idxs[mid]
            elif filter_words[mid] > s:
                right = mid - 1
            else:
                left = mid + 1
        return -1
