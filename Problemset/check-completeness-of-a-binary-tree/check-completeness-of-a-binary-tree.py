
# @Title: 二叉树的完全性检验 (Check Completeness of a Binary Tree)
# @Author: cocofe
# @Date: 2021-01-01 18:53:25
# @Runtime: 32 ms
# @Memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return False
        q = collections.deque()
        q.append(root)
        nums = []
        idx = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                nums.append((idx, node is not None))
                idx += 1
                if node:
                    q.append(node.left)
                    q.append(node.right)
        # print nums
        is_False = False
        for idx, node in nums:
            if is_False and node:
                return False
            if not node:
                is_False = True
        return True
        
            


            
