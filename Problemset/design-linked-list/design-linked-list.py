
# @Title: 设计链表 (Design Linked List)
# @Author: cocofe
# @Date: 2020-11-02 21:39:09
# @Runtime: 264 ms
# @Memory: 15.3 MB

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def show(self):
        p = self.head
        nums = []
        while p:
            nums.append(str(p.val) if p.val is not None else 'null')
            p = p.next
        print '<->'.join(nums)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self.index_of(index)
        return node.val if node else -1

    def index_of(self, index):
        if index >= self.len:
            return None
        if index < self.len / 2:
            p = self.head
            idx = -1
            while p and idx != index:
                idx += 1
                p = p.next
        else:
            p = self.tail
            idx = self.len
            while p and idx != index:
                idx -= 1
                p = p.prev
        return p

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.len += 1
        nex = self.head.next
        node = Node(val)
        node.prev = self.head
        self.head.next = node
        node.next = nex
        nex.prev = node
        # print 'addAtHead ', val
        # self.show()

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.len += 1
        # print 'addAtTail ', val, self.len
        # self.show()

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.index_of(index)
        if not curr: 
            if index > self.len:
                return
            elif index < 0:
                return self.addAtHead(val)
            elif index == self.len:
                return self.addAtTail(val)
        self.len += 1
        curr = curr.prev
        node = Node(val)
        nex = curr.next
        curr.next = node
        node.prev = curr
        node.next = nex
        nex.prev = node
        # print 'addAtIndex ', index, val
        # self.show()

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        curr = self.index_of(index)
        if not curr: return
        prev = curr.prev
        prev.next = curr.next
        if curr.next:
            curr.next.prev = prev
        self.len -= 1
        # print 'deleteAtIndex ', index, self.len
        # self.show()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
