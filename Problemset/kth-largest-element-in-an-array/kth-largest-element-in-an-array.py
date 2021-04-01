
# @Title: 数组中的第K个最大元素 (Kth Largest Element in an Array)
# @Author: cocofe
# @Date: 2021-03-28 15:57:00
# @Runtime: 44 ms
# @Memory: 13.9 MB

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 大小为k的小根堆, 堆顶为k个中最小
        heap = []
        for idx, num in enumerate(nums):
            if idx < k:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heappushpop(heap, num)
        return heap[0]

