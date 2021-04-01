
# @Title: 二叉搜索树的最近公共祖先 (Lowest Common Ancestor of a Binary Search Tree)
# @Author: cocofe
# @Date: 2020-09-30 23:45:37
# @Runtime: 68 ms
# @Memory: 20.4 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = []
        def trace(path, optional, target):
            if not optional:
                return
            for seleted in optional:
                tmp = path[:]
                path.append(seleted)
                if seleted.val == target.val:
                    ans.append(path)
                    return
                _op = []
                # 基于有序特性, 确定往哪个节点遍历
                if seleted.left and target.val < seleted.val:
                    _op.append(seleted.left)
                elif seleted.right and target.val > seleted.val:
                    _op.append(seleted.right)
                trace(path, _op, target)
                path = tmp
        if not root: return
        trace([], [root], p)
        trace([], [root], q)
        length = min(map(len, ans))
        _ans = None
        for i in range(0, length):
            if ans[0][i].val == ans[1][i].val:
                _ans = ans[0][i]
            else:
                break
        return _ans

