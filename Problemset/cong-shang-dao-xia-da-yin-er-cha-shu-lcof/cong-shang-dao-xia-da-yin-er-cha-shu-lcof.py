
# @Title: 从上到下打印二叉树 (从上到下打印二叉树 LCOF)
# @Author: cocofe
# @Date: 2020-08-16 23:21:08
# @Runtime: 24 ms
# @Memory: 13 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        ans, queue = [], deque()
        if not root: return ans
        queue.append(root)
        while queue:
            node = queue.popleft()
            ans.append(node.val)
            # inspect 速度慢!!
            # attrs = ['left', 'right']
            # for attr in attrs:
            #     if getattr(node, attr):
            #         queue.append(getattr(node, attr))
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return ans
