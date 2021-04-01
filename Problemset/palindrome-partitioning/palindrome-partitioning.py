
# @Title: 分割回文串 (Palindrome Partitioning)
# @Author: cocofe
# @Date: 2021-03-07 11:38:55
# @Runtime: 152 ms
# @Memory: 49.7 MB

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_hw(string):
            return string == string[::-1]
        ret = []
        def backtrace(string, idx, ans):
            if idx >= len(s):
                # 所有的子串都是回文串才是一个可选答案
                if ''.join(ans) == s:
                    ret.append(ans)
                return
            to_choice = s[idx]
            if is_hw(string+to_choice):
                tmp = ans[::]
                if is_hw(string):
                    tmp.pop()
                tmp.append(string+to_choice)
                backtrace(string+to_choice, idx + 1, tmp)
            else:
                # 不是回文串, 也需要加入, 因为后续加入其它字符串后, 可能就变成会回文串了
                tmp = ans[::]
                if is_hw(string):
                    tmp.pop()
                backtrace(string+to_choice, idx + 1, tmp)
            ans.append(to_choice)
            backtrace(to_choice, idx + 1, ans)
        for idx in range(1, len(s)+1):
            if is_hw(s[0:idx]):
                backtrace(s[0:idx], idx, [s[0:idx]])
            break
        return ret
