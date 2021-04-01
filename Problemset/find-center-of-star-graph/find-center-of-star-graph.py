
# @Title: 找出星型图的中心节点 (Find Center of Star Graph)
# @Author: cocofe
# @Date: 2021-03-14 11:44:51
# @Runtime: 160 ms
# @Memory: 44.3 MB

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        idx, nex = 0, 1
        ans = collections.defaultdict(int)
        for i, j in edges:
            ans[i] += 1
            ans[j] += 1
        for i, count in ans.items():
            if count == len(ans) - 1:
                return i
        return -1
