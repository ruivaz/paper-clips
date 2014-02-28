def rotate_left(list, n):
  return list[n:]+list[:n]

def rotate_right(list, n):
  return list[len(list)-n:] + list[:len(list)-n]

list=[1,4,6,3,4,7]
print list
print rotate_left(list, 2)
print rotate_right(list, 2)
