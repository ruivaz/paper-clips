import time

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start

def follow(thefile, target):
  thefile.seek(0,2)
  while True:
    line = thefile.readline()
    if not line:
      time.sleep(0.1)
      continue
    target.send(line)

@coroutine
def grep(pattern, target):
  while True:
    line = (yield)
    if pattern in line:
      target.send(line)

@coroutine
def printer():
  while True:
    line = (yield)
    print line

@coroutine
def broadcast(targets):
  while True:
    item = (yield)
    for target in targets:
      target.send(item)

f = open('hello.log')
follow(f, 
	broadcast([grep('Hello', printer()),
		   grep('python', printer()),
                   grep('Monday', printer())])
 )
