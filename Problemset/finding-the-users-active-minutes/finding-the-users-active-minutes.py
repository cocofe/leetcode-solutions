
# @Title: 查找用户活跃分钟数 (Finding the Users Active Minutes)
# @Author: cocofe
# @Date: 2021-04-04 11:23:01
# @Runtime: 144 ms
# @Memory: 21.9 MB

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        mapping = collections.defaultdict(set)
        for id, ms in logs:
            mapping[id].add(ms)
        for _, mss in mapping.items():
            ans[len(mss)-1] += 1
        return ans

