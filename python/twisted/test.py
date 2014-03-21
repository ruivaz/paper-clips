def number_generator():
  i=0
  while(i<61):
    yield i
    i += 1

def switch(value):
  if value == phase[0]:
    return phase[1]
  else:
    return phase[0]  
  

period = 5
phase = ['lower', 'higher']
value = phase[0]

for i in number_generator():
  if i%5 == 0:
    value = switch(value)
  print str(i) + " " + value  
