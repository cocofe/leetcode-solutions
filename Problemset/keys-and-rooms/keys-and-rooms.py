
# @Title: 钥匙和房间 (Keys and Rooms)
# @Author: cocofe
# @Date: 2020-08-31 23:51:17
# @Runtime: 56 ms
# @Memory: 12.9 MB

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        q = collections.deque()
        q.append(0)
        while q:
            idx = q.popleft()
            keys = rooms[idx]
            visited.add(idx)
            for key in keys:
                if key not in visited:
                    q.append(key)
        return len(visited) == len(rooms)
                
        
