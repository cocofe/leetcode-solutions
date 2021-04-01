
# @Title: 最大平均通过率 (Maximum Average Pass Ratio)
# @Author: cocofe
# @Date: 2021-03-14 16:20:59
# @Runtime: 3440 ms
# @Memory: 49.9 MB

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        diff = lambda pas,total: float(pas+1) / (total+1) - float(pas) / (total)
        heap = []
        ans = 0
        for pas, total in classes:
            ans += float(pas) / total
            heap.append((-diff(pas, total), pas, total))
        heapq.heapify(heap)
        for _ in range(extraStudents):
            df, pas, total = heapq.heappop(heap)
            ans += -df
            heapq.heappush(heap, (-diff(pas+1, total+1), pas+1, total+1))
        return ans / len(classes)
        
        
