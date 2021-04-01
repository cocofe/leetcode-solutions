
# @Title: 最后一个单词的长度 (Length of Last Word)
# @Author: cocofe
# @Date: 2020-07-09 20:57:19
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = -1
        length = len(s)
        ans = 0
        while abs(idx) <= length:
            if ans == 0 and s[idx] == ' ':
                idx -= 1
                continue
            if ans > 0 and s[idx] == ' ':
                break
            ans += 1
            idx -= 1
        return ans


        

