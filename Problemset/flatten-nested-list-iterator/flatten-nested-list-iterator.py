
# @Title: 扁平化嵌套列表迭代器 (Flatten Nested List Iterator)
# @Author: cocofe
# @Date: 2021-03-23 00:55:05
# @Runtime: 80 ms
# @Memory: 18.8 MB

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = collections.deque()
        for node in nestedList:
            self.stack.append(node)

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.popleft()
        if isinstance(node, int):
            return node
        if node.isInteger():
            self.stack.appendleft(node.getInteger())
        else:
            self.stack.extendleft(node.getList()[::-1])
        return self.next()

    def _has_next(self, node):
        if not node:
            return False
        if node.isInteger():
            return True
        for n in node.getList():
            if self._has_next(n):
                return True
        return False
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return False
        while self.stack:
            node = self.stack[0]
            if self._has_next(node):
                return True
            self.stack.popleft()
        return False
        
        
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
