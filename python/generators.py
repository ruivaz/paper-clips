def cubic_generator(n):
  for i in range(n):
    yield i ** 3


for i in cubic_generator(10):
  print i
