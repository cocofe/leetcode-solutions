
# @Title: 二叉树的右视图 (Binary Tree Right Side View)
# @Author: cocofe
# @Date: 2021-02-07 01:21:30
# @Runtime: 28 ms
# @Memory: 13 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = collections.deque()
        ans = []
        if not root:
            return ans
        queue.append(root)
        while queue:
            last_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                last_node = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(last_node)
        return ans
