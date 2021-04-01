
# @Title: 最长字符串链 (Longest String Chain)
# @Author: cocofe
# @Date: 2020-12-12 14:05:27
# @Runtime: 1096 ms
# @Memory: 13.4 MB

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def is_match(w1, w2):
            # length w1 > w2
            for i, w in enumerate(w2):
                if w == w1[i]:
                    continue
                w1 = w1[:i]+w1[i+1:]
                break
            return w1[:len(w2)] == w2

        words = sorted(words, key=lambda w:len(w))
        dp = collections.defaultdict(lambda:1)
        ans = 1
        for i, word in enumerate(words):
            j = i-1
            while j >= 0:
                w = words[j]
                if len(w) < len(word) - 1:
                    break
                # print word, w, is_match(word, w)
                if len(w) == len(word) - 1 and is_match(word, w):
                    dp[i] = max(dp[j]+1, dp[i])
                j -= 1
            ans = max(ans, dp[i])
        return ans
            

                    

