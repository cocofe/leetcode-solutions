
# @Title: 前K个高频单词 (Top K Frequent Words)
# @Author: cocofe
# @Date: 2021-04-01 01:47:23
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words)
        heap = []
        for key, cnt in counter.items():
            heapq.heappush(heap, (-cnt, key))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
