def intersect(list1, list2):
  size1=len(list1)
  size2=len(list2)
  i=0
  j=0
  result = []
  
  while i<size1 and j<size2:
    if list1[i] == list2[j]:
      result.append(list1[i])
      j+=1
      i+=1
    elif list1[i] > list2[j]:
      j+=1
    else:
      i+=1

  return result;


a=[1,4,7,9,12]
b=[4,9,13]
print intersect(a, b)
