
# @Title: 按序打印 (Print in Order)
# @Author: cocofe
# @Date: 2021-03-23 21:24:39
# @Runtime: 40 ms
# @Memory: 13 MB

class Foo(object):
    def __init__(self):
        self.cv = threading.Condition()
        self.flag = 1


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        with self.cv:
            while self.flag != 1:
                self.cv.wait()
            printFirst()
            self.flag += 1


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.cv:
            while self.flag != 2:
                self.cv.wait()
            printSecond()
            self.flag += 1
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.cv:
            while self.flag != 3:
                self.cv.wait()
            printThird()
