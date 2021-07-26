
# @Title: 可以输入的最大单词数 (Maximum Number of Words You Can Type)
# @Author: cocofe
# @Date: 2021-07-18 10:46:40
# @Runtime: 36 ms
# @Memory: 15.1 MB

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        nums = text.split(" ")
        ans = 0
        for s in nums:
            if set(s) & set(brokenLetters):
                continue
            ans += 1
        return ans
