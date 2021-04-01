
# @Title: 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# @Author: cocofe
# @Date: 2020-04-02 01:38:10
# @Runtime: 28 ms
# @Memory: N/A

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
        :rtype: List[List[int]]
        """
        ans = {}
        def helper(root, lever):
            if not root:
                return None
            ans.setdefault(lever, [])
            ans[lever].append(root.val)
            helper(root.left, lever+1)
            helper(root.right, lever+1)
        helper(root, 0)
        ret = []
        for lever in sorted(ans):
            ret.append(ans[lever])
        return ret
            
        
        
        
        
