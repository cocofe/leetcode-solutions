
# @Title: 最接近原点的 K 个点 (K Closest Points to Origin)
# @Author: cocofe
# @Date: 2020-11-09 00:44:47
# @Runtime: 560 ms
# @Memory: 18.7 MB

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points = sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]

