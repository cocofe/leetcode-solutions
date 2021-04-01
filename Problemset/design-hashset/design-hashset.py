
# @Title: 设计哈希集合 (Design HashSet)
# @Author: cocofe
# @Date: 2021-03-13 01:17:02
# @Runtime: 524 ms
# @Memory: 19.5 MB

class Node(object):

    def __init__(self, value):
        self.val = value
        self.next = None


class MyHashSet(object):

    length = 10000

    def _hash(self, key):
        return hash(key) % self.length

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [-1] * self.length


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        node = self.data[self._hash(key)]
        if not self.contains(key):
            if node == -1:
                self.data[self._hash(key)] = Node(key)
            else:
                while node.next:
                    node = node.next
                node.next = Node(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            node = self.data[self._hash(key)]
            head = Node(0)
            prev = head
            prev.next = node
            while node:
                if node.val == key:
                    prev.next = node.next
                    break
                else:
                    prev = node
                    node = node.next
            if head.next:
                self.data[self._hash(key)] = head.next
            else:
                self.data[self._hash(key)] = -1


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        val = self.data[self._hash(key)]
        if val == -1:
            return False
        else:
            p = val
            while p:
                if p.val == key:
                    return True
                p = p.next
            return False
        



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
