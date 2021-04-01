
# @Title: 实现 strStr() (Implement strStr())
# @Author: cocofe
# @Date: 2020-09-28 01:40:51
# @Runtime: 456 ms
# @Memory: 119 MB

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        import string
        from collections import defaultdict
        def kmp(pat):
            # 定义 dp[i][j] = x 
            # 表示: 在pat某个索引位置下, 碰到字符j的下一个pat索引位置
            dp = defaultdict(lambda: defaultdict(int))
            prev_status_idx = 0
            status_idx = 0
            dp[0][pat[0]] = 1
            for status_idx in range(1, len(pat)):
                for c in string.ascii_letters:
                    if c == pat[status_idx]:
                        dp[status_idx][c] = status_idx + 1
                    else:
                        dp[status_idx][c] = dp[prev_status_idx][c]
                prev_status_idx = dp[prev_status_idx][pat[status_idx]]
            return dp
        dp = kmp(needle)
        idx = 0
        p_idx = 0
        while idx < len(haystack):
            p_idx = dp[p_idx][haystack[idx]]
            if p_idx == len(needle):
                return idx - p_idx + 1
            idx += 1
        return -1
            
                
