list1 = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6]

def mult(l):
  if l>0:
    return 1
  else: 
    return 0


result = filter(mult, list1)

print result
