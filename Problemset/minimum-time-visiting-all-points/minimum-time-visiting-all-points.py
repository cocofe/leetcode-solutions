
# @Title: 访问所有点的最小时间 (Minimum Time Visiting All Points)
# @Author: cocofe
# @Date: 2020-02-01 15:24:55
# @Runtime: 840 ms
# @Memory: N/A

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        idx = 0
        while idx + 1 < len(points):
            x, y = points[idx]
            nx, ny = points[idx + 1]
            while nx != x or ny != y:
                if x < nx:
                    x += 1
                elif x > nx:
                    x -= 1
                if y < ny:
                    y += 1
                elif y > ny:
                    y -= 1
                count += 1
            idx += 1
            
        return count
            
        
