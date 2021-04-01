
# @Title: H2O 生成 (Building H2O)
# @Author: cocofe
# @Date: 2021-03-23 22:50:48
# @Runtime: 20 ms
# @Memory: 13.4 MB

class H2O(object):
    def __init__(self):
        self.h_semaphore = threading.Semaphore(2)
        self.flag = 0
        self.o_semaphore = threading.Semaphore(0)


    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h_semaphore.acquire()
        self.flag += 1
        releaseHydrogen()
        if self.flag % 2 == 0:
            self.o_semaphore.release()


    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.o_semaphore.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h_semaphore.release()
        self.h_semaphore.release()

