
# @Title: 设计哈希映射 (Design HashMap)
# @Author: cocofe
# @Date: 2021-03-14 00:32:55
# @Runtime: 804 ms
# @Memory: 16.9 MB

class Node(object):

    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None

class MyHashMap(object):

    length = 1000

    def _hash(self, key):
        return hash(key) % self.length

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [-1] * self.length


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        slots = self.data[self._hash(key)]
        node = self.get(key)
        if node == -1:
            if slots == -1:
                self.data[self._hash(key)] = Node(key, value)
            else:
                while slots.next:
                    slots = slots.next
                slots.next = Node(key, value)
        else:
            while slots:
                if slots.key == key:
                    slots.val = value
                    break
                slots = slots.next


            


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        val = self.data[self._hash(key)]
        if val == -1:
            return -1
        else:
            p = val
            while p:
                if p.key == key:
                    return p.val
                p = p.next
            return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if self.get(key) != -1:
            node = self.data[self._hash(key)]
            head = Node(0, 0)
            prev = head
            prev.next = node
            while node:
                if node.key == key:
                    prev.next = node.next
                    break
                else:
                    prev = node
                    node = node.next
            if head.next:
                self.data[self._hash(key)] = head.next
            else:
                self.data[self._hash(key)] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
