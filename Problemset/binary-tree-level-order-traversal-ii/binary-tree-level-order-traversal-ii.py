
# @Title: 二叉树的层序遍历 II (Binary Tree Level Order Traversal II)
# @Author: cocofe
# @Date: 2020-09-06 14:40:58
# @Runtime: 16 ms
# @Memory: 12.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        levels.append([root])
        while True:
            level = levels[-1]
            if not any(level):
                break
            next_level = []
            for node in level:
                if not node:
                    continue
                next_level.extend([node.left, node.right])
            levels.append(next_level)
        ans = []
        levels.reverse()
        for level in levels:
            _ans = []
            for node in level:
                if not node:
                    continue
                _ans.append(node.val)
            if _ans:
                ans.append(_ans)
        return ans
