
# @Title: 二叉树最大宽度 (Maximum Width of Binary Tree)
# @Author: cocofe
# @Date: 2021-04-02 00:58:58
# @Runtime: 20 ms
# @Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        注意理解题意
        就是计算每层首尾不为空的节点及其之前的元素个数(包含空节点)
        """
        if not root: return 0
        q = collections.deque()
        q.append((root, 0, 0))
        ans = 0
        while q:
            left = None
            for _ in range(len(q)):
                node, depth, pos = q.popleft()
                if left is None:
                    left = pos
                if node.left:
                    q.append((node.left, depth+1, pos * 2 + 1))
                if node.right:
                    q.append((node.right, depth+1, pos * 2 + 2))
                ans = max(ans, pos - left + 1)
        return ans

                    
                    
