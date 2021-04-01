
# @Title: 常数时间插入、删除和获取随机元素 (Insert Delete GetRandom O(1))
# @Author: cocofe
# @Date: 2020-09-29 22:33:51
# @Runtime: 296 ms
# @Memory: 16.9 MB

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_idx_map = {}
        self.values = []
        self.length = 0


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        idx = self.val_idx_map.get(val)
        if idx is not None:
            return False
        self.values.append(val)
        self.val_idx_map[val] = self.length
        self.length += 1
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        idx = self.val_idx_map.get(val)
        if idx is None:
            return False
        # swap
        self.values[idx], self.values[self.length-1] = self.values[self.length-1], self.values[idx]
        self.val_idx_map[self.values[idx]] = idx
        self.val_idx_map.pop(self.values[self.length-1], None)
        self.values.pop()
        self.length -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.length-1)
        return self.values[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
