
# @Title: 前 K 个高频元素 (Top K Frequent Elements)
# @Author: cocofe
# @Date: 2021-02-24 03:17:28
# @Runtime: 36 ms
# @Memory: 14.9 MB

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        heap = []
        for key, count in counter.items():
            heapq.heappush(heap, (count, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
