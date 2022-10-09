from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.sem = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.sem.release()
            with self.sem:
                pass

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):

            # printBar() outputs "bar". Do not change or remove this line.
        	printBar()
