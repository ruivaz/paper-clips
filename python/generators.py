import sys

def cubic_generator(n):
  for i in range(n):
    yield i ** 3


def fibonaci(n):
  if(n<3): return n
  else: return fibonaci(n-1)+fibonaci(n-2) 


def n_fibonaci(n):
  for i in range(n):
    yield fibonaci(i)  

for i in cubic_generator(10):
  print i

i=0
for i in n_fibonaci(int(sys.argv[1])):
  i+=i

print i

