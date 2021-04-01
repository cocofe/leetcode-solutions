
# @Title: 打印零与奇偶数 (Print Zero Even Odd)
# @Author: cocofe
# @Date: 2021-03-23 01:43:21
# @Runtime: 44 ms
# @Memory: 14.3 MB

from threading import Condition
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        # - 0: print 0
        # - 1: print odd
        # - 2: print even
        self.flag = 0
        self.cond = Condition()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            with self.cond:
                # 不知为什么用if会导致出错, flag在printnumber的时候会被修改
                while self.flag != 0:
                    self.cond.wait()
                printNumber(0)
                self.flag = 2 if i % 2 == 0 else 1
                self.cond.notify_all()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n + 1, 2):
            with self.cond:
                while self.flag != 2:
                    self.cond.wait()
                printNumber(i)
                self.flag = 0
                self.cond.notify_all()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1, 2):
            with self.cond:
                while self.flag != 1:
                    self.cond.wait()
                printNumber(i)
                self.flag = 0
                self.cond.notify_all()
