
# @Title: 最长单词 (Longest Word LCCI)
# @Author: cocofe
# @Date: 2021-04-28 01:09:45
# @Runtime: 48 ms
# @Memory: 15.2 MB

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda word: (-len(word), word))
        cache = set(words)
        def backtrack(s, is_head=False):
            if not s:
                return True
            idx = 0
            while idx < len(s):
                if is_head and idx + 1 == len(s):
                    break
                sub_s = s[:idx+1]
                if sub_s in cache and backtrack(s[idx+1:]):
                    return True
                idx += 1
            return False
        for word in words:
            if backtrack(word, is_head=True):
                return word
        return ''
            
                    
