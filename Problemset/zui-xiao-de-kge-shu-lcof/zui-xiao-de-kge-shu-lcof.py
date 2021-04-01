
# @Title: 最小的k个数 (最小的k个数  LCOF)
# @Author: cocofe
# @Date: 2021-01-01 22:40:42
# @Runtime: 112 ms
# @Memory: 14.4 MB

class Solution(object):

    def heapify(self, arr, size, i):
        left, right = i * 2 + 1, i * 2 + 2
        largest = i
        if left < size and arr[largest] < arr[left]:
            largest = left
        if right < size and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            self.swap(arr, largest, i)
            self.heapify(arr, size, largest)
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def build_max_heap(self, arr, k):
        last_no_leaf_node = (k - 2) / 2
        nums = arr[:k]
        for i in range(last_no_leaf_node, -1, -1):
            self.heapify(nums, k, i)
        return nums

    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0: return []
        nums = self.build_max_heap(arr, k)
        for i in range(k, len(arr)):
            if arr[i] >= nums[0]:
                continue
            nums[0] = arr[i]
            self.heapify(nums, k, 0)
        return nums
