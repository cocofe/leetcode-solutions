
# @Title: 树的子结构 (树的子结构  LCOF)
# @Author: cocofe
# @Date: 2020-10-25 00:43:00
# @Runtime: 104 ms
# @Memory: 22.6 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not B: return False
        def track(node1, node2):
            # print node1, node2
            if not node2:
                return True
            if not all([node1, node2]):
                return False
            if node1.val != node2.val:
                return False
            return all([track(node1.left, node2.left), track(node1.right, node2.right)])
        ans = [False]
        def dfs(node):
            if ans[0]:
                return
            if not node:
                return 
            if node.val == B.val:
                if track(node, B):
                    ans[0] = True
                    return True
            dfs(node.left)
            dfs(node.right)
            return False
        dfs(A)
        return ans[0]
