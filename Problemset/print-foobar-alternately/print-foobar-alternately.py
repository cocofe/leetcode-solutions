
# @Title: 交替打印FooBar (Print FooBar Alternately)
# @Author: cocofe
# @Date: 2021-03-23 22:39:52
# @Runtime: 56 ms
# @Memory: 15.1 MB

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_semaphore = threading.Semaphore(1)
        self.bar_semaphore = threading.Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_semaphore.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_semaphore.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_semaphore.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_semaphore.release()
