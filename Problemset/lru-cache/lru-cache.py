
# @Title: LRU 缓存机制 (LRU Cache)
# @Author: cocofe
# @Date: 2021-01-12 20:58:56
# @Runtime: 4396 ms
# @Memory: 23 MB

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return '{} -> <Node({})> -> {}'.format(self.prev, self.val, self.next)


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.cache = {}
        self.head = Node(None)

    def find_node(self, val):
        p = self.head.next
        visited = []
        while p:
            visited.append(p.val)
            if p.val == val:
                break 
            p = p.next
        # print 'find val {}, visited {}'.format(val, visited)
        return p

    def insert_to_head(self, node):
        nex = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nex
        if nex:
            nex.prev = node
    
    def pop_node(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        if nex:
            nex.prev = prev

    def move_to_head(self, key):
        node = self.find_node(key)
        if not node:
            print 'not found key {} node in cache {} len {}'.format(key, self.cache, self.length)
            return
        self.pop_node(node)
        self.insert_to_head(node)

    def pop_end_node(self):
        p = self.head.next
        prev = None
        while p:
            prev = p
            p = p.next
        self.cache.pop(prev.val)
        self.pop_node(prev)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.move_to_head(key)   
        return self.cache[key] 

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.move_to_head(key) 
        else:
            if self.length == self.capacity:
                self.pop_end_node()
                self.length -= 1
            self.insert_to_head(Node(key))
            self.length += 1
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
