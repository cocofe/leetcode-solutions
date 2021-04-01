
# @Title: 从上到下打印二叉树 II (从上到下打印二叉树 II LCOF)
# @Author: cocofe
# @Date: 2020-08-16 23:14:47
# @Runtime: 28 ms
# @Memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(node):
        if not node: return
        
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, q = [], collections.deque()
        if not root: return ans
        q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(tmp)
        return ans





