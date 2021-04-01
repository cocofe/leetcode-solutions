
# @Title: 二叉树的所有路径 (Binary Tree Paths)
# @Author: cocofe
# @Date: 2020-09-30 23:03:42
# @Runtime: 24 ms
# @Memory: 12.4 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        def trace(path, optional):
            if not optional:
                ans.append(path)
                return
            for selected in optional:
                tmp = path[:]
                path.append(str(selected.val))
                _op = []
                if selected.left:
                   _op.append(selected.left) 
                if selected.right:
                    _op.append(selected.right) 
                trace(path, _op)
                path = tmp
        if not root: return ans
        trace([], [root])
        return ["->".join(_ans) for _ans in ans]
