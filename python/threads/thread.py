from threading import Thread

class myObject(object):
    def __init__(self):
        self.val=1
    def get(self):
        return self.val
    def increment(self):
        self.val += 1

def t1(ob):
    ob.increment()
    print 't1:', ob.get()==2

def t2(ob):
    ob.increment()
    print 't2:', ob.get()==2

obj = myObject()
thread1 = Thread(target=t1, args=(obj,))
thread2 = Thread(target=t2, args=(obj,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
