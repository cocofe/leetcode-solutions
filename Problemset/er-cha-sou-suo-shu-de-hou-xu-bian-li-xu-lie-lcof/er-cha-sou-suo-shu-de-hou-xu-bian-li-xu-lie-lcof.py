
# @Title: 二叉搜索树的后序遍历序列 (二叉搜索树的后序遍历序列 LCOF)
# @Author: cocofe
# @Date: 2020-08-17 00:40:23
# @Runtime: 20 ms
# @Memory: 12.4 MB

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def helper(start, end):
            if start >= end: return True
            root_idx = end
            p = start
            while postorder[p] < postorder[end]: p += 1
            right_tree_start_idx = p
            while postorder[p] > postorder[end]: p += 1
            # 判断是否是二叉搜索数, 对于后序遍历序列一定有
            # - 左子树元素 <= 根节点 <= 右子树
            # - 最右边的元素是根节点
            # - 存在一个元素>根节点, 该元素后面的元素都大于根节点 
            return p == end and helper(start, right_tree_start_idx - 1) and helper(right_tree_start_idx, end - 1)

        return helper(0, len(postorder) - 1)
