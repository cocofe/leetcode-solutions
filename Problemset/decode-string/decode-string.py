
# @Title: 字符串解码 (Decode String)
# @Author: cocofe
# @Date: 2020-11-06 22:47:31
# @Runtime: 8 ms
# @Memory: 13.1 MB

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        char_stack = []
        ans = []
        idx = 0
        while idx < len(s):
            _s = s[idx]
            if _s.isdigit():
                num = []
                while _s.isdigit() and idx < len(s):
                    num.append(_s)
                    idx += 1
                    _s = s[idx]
                num_stack.append(int(''.join(num)))
                idx -= 1
            elif _s == ']':
                # pop 知道碰到[
                tmp = []
                while char_stack:
                    c = char_stack.pop()
                    if c == '[':
                        break
                    tmp.append(c)
                tmp = tmp[::-1]
                count = num_stack.pop()
                tmp *= count
                if char_stack:
                    char_stack += tmp
                    # print char_stack
                else:
                    ans += tmp
                    # print 'ans: ', ans
            else:
                if char_stack or _s == '[':
                    char_stack.append(_s)
                else:
                    ans.append(_s)
            idx += 1
        return ''.join(ans)
