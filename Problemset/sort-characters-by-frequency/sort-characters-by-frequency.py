
# @Title: 根据字符出现频率排序 (Sort Characters By Frequency)
# @Author: cocofe
# @Date: 2021-07-03 00:27:46
# @Runtime: 44 ms
# @Memory: 15.4 MB

class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        heap = []
        heapq.heapify(heap)
        for char, cnt in count.items():
            heapq.heappush(heap, (-cnt, char))
        ans = []
        while heap:
            cnt, char = heapq.heappop(heap)
            ans.append(char * (0 - cnt))
        return ''.join(ans)

