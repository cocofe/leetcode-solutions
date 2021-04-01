
# @Title: 去除重复字母 (Remove Duplicate Letters)
# @Author: cocofe
# @Date: 2020-11-15 23:36:48
# @Runtime: 28 ms
# @Memory: 13.4 MB

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        stack = []
        used = {}
        for char in s:
            if char in used:
                counter[char] -= 1
                continue
            while stack and stack[-1] >= char and counter.get(stack[-1]) > 1:
                _c = stack[-1]
                counter[_c] -= 1
                stack.pop()
                used.pop(_c)
            stack.append(char)
            used[char] = True
        return ''.join(stack)
