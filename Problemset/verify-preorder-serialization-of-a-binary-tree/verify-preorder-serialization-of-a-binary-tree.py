
# @Title: 验证二叉树的前序序列化 (Verify Preorder Serialization of a Binary Tree)
# @Author: cocofe
# @Date: 2021-03-12 02:19:19
# @Runtime: 32 ms
# @Memory: 13 MB

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = [1]
        idx = 0
        while idx < len(preorder):
            s = preorder[idx]
            if not stack:
                return False
            if s == ',':
                idx += 1
            elif s == '#':
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                idx += 1
            else:
                while idx < len(preorder) and preorder[idx] != ',':
                    idx += 1
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                stack.append(2)
        return not stack
