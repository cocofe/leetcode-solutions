
# @Title: 删除字符串中的所有相邻重复项 (Remove All Adjacent Duplicates In String)
# @Author: cocofe
# @Date: 2021-03-09 00:29:15
# @Runtime: 64 ms
# @Memory: 13.7 MB

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
                continue
            stack.append(s)
        return ''.join(stack)
            
