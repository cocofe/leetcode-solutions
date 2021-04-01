
# @Title: 最小K个数 (Smallest K LCCI)
# @Author: cocofe
# @Date: 2021-03-31 23:14:31
# @Runtime: 140 ms
# @Memory: 20.1 MB

class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 求前k小, 维护一个大小为k的大根堆,
        # 如果 元素比当前堆中最大值还要小, 则放入堆中, 保证小的元素都放入堆中, 则堆中是第k小
        if k == 0: return []
        heap = []
        for idx, num in enumerate(arr):
            if idx < k:
                heapq.heappush(heap, -num)
            elif -heap[0] > num:
                heapq.heappushpop(heap, -num)
        return [-num for num in heap]
