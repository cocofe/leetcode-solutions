
# @Title: 课程表 (Course Schedule)
# @Author: cocofe
# @Date: 2021-04-04 18:56:17
# @Runtime: 416 ms
# @Memory: 15.5 MB

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indegree = [0] * numCourses
        for i, j in prerequisites:
            edges[j].append(i)
            indegree[i] += 1
        q = collections.deque()
        visited = set()
        for idx, ind in enumerate(indegree):
            if ind == 0:
                q.append(idx)
                visited.add(idx)
        learned = 0
        while q:
            course = q.popleft()
            for c in edges[course]:
                indegree[c] -= 1
            for idx, ind in enumerate(indegree):
                if ind == 0 and idx not in visited:
                    q.append(idx)
                    visited.add(idx)
            learned += 1
        return learned == numCourses
