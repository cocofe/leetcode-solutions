
# @Title: 哪种连续子字符串更长 (Longer Contiguous Segments of Ones than Zeros)
# @Author: cocofe
# @Date: 2021-05-23 10:45:41
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if len(s) == 1:
            return s == '1'
        c1 = 0
        c0 = 0
        idx = 0
        while idx < len(s):
            cnt = 0
            head = s[idx]
            while idx + 1 < len(s) and s[idx+1] == s[idx]:
                idx += 1
                cnt += 1
            if head == '0':
                c0 = max(c0, cnt)
            else:
                c1 = max(c1, cnt)
            idx += 1
        return c1 > c0
        
