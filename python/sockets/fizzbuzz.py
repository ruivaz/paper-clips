for i in range(0, 101):

  msg= ''  
  if i % 3 == 0:
    msg += 'Fizz'
  if i % 5 == 0:
    msg += 'Buzz'

  print msg or i
  
