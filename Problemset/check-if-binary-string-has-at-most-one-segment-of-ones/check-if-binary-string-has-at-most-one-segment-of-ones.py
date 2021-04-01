
# @Title: 检查二进制字符串字段 (Check if Binary String Has at Most One Segment of Ones)
# @Author: cocofe
# @Date: 2021-03-07 10:43:52
# @Runtime: 32 ms
# @Memory: 15 MB

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        idx = 0
        while idx < len(s):
            if s[idx] == '0':
                idx += 1
                continue
            idx += 1
            while idx < len(s) and s[idx] == '1':
                idx += 1
            count += 1
            
        return count == 1
            
            
