
# @Title: 交替打印字符串 (Fizz Buzz Multithreaded)
# @Author: cocofe
# @Date: 2021-03-23 10:24:00
# @Runtime: 28 ms
# @Memory: 13.1 MB

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.curr = 1
        self.cv = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        while self.curr <= self.n:
            with self.cv:
                while not (self.curr % 3 == 0 and self.curr % 5 != 0) and not self.is_end():
                    # print 'fizz; wait curr %s' % self.curr
                    self.cv.wait(timeout=1)
                if self.is_end():
                    break
                printFizz()
                self.curr += 1
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        while self.curr <= self.n:
            with self.cv:
                while not (self.curr % 3 != 0 and self.curr % 5 == 0) and not self.is_end():
                    # print 'buzz; wait curr %s' % self.curr
                    self.cv.wait(timeout=1)
                if self.is_end():
                    break
                printBuzz()
                self.curr += 1
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        while self.curr <= self.n:
            with self.cv:
                while not (self.curr % 3 == 0 and self.curr % 5 == 0) and not self.is_end():
                    # print 'fizzbuzz; wait curr %s' % self.curr
                    self.cv.wait(timeout=1)
                if self.is_end():
                    break
                printFizzBuzz()
                self.curr += 1
                self.cv.notify_all()

    def is_end(self):
        return self.curr > self.n

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while self.curr <= self.n:
            with self.cv:
                while not (self.curr % 3 != 0 and self.curr % 5 != 0) and not self.is_end():
                    # print 'number; wait curr %s' % self.curr
                    self.cv.wait(timeout=1)
                if self.is_end():
                    break
                printNumber(self.curr)
                self.curr += 1
                self.cv.notify_all()
