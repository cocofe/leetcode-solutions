
# @Title: 求根节点到叶节点数字之和 (Sum Root to Leaf Numbers)
# @Author: cocofe
# @Date: 2020-10-29 00:11:11
# @Runtime: 24 ms
# @Memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def track(path, choices):
            if not choices:
                ans.append(int(''.join(path)))
                return
            for node in choices:
                tmp = path[:]
                _choices = []
                path.append(str(node.val))
                if node.left:
                    _choices.append(node.left)
                if node.right:
                    _choices.append(node.right)
                track(path, _choices)
                path = tmp
        if root:
            track([], [root])
        return sum(ans)
