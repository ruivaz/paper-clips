def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start

@coroutine 
def grep(pattern):
    print 'Looking for ' + pattern
    try:
        while True:
            line = (yield)
            if pattern in line:
                print line,    
    except GeneratorExit:
        print "Going Away. Goodbye"
