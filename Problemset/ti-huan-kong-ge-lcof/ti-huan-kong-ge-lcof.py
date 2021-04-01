
# @Title: 替换空格 (替换空格 LCOF)
# @Author: cocofe
# @Date: 2020-08-10 23:29:06
# @Runtime: 16 ms
# @Memory: 12.4 MB

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        extra_space = 0
        for i in s:
            if i == ' ':
                extra_space += 2
        ans = [0] * (len(s) + extra_space)
        idx = 0
        ans_idx = 0
        while idx < len(s):
            if s[idx] == ' ':
                ans[ans_idx] = '%'
                ans[ans_idx+1] = '2'
                ans[ans_idx+2] = '0'
                ans_idx += 3
            else:
                ans[ans_idx] = s[idx]
                ans_idx += 1
            idx += 1
        return ''.join(ans)
