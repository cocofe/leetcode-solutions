
# @Title: 二叉树的锯齿形层序遍历 (Binary Tree Zigzag Level Order Traversal)
# @Author: cocofe
# @Date: 2021-04-01 23:10:30
# @Runtime: 28 ms
# @Memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        reverse = 0
        q = collections.deque()
        ans = []
        if not root:
            return ans
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                level.reverse()
            ans.append(level)
            reverse = not reverse
        return ans


