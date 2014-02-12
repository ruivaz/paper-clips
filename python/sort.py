def swap(list, left, right):
  tmp=list[left]
  list[left]=list[right]
  list[right]=tmp

def partition(list, left, right):
  pivot = list[left]
  while left<right:
    while list[left]<pivot:
      left+=1
    while list[right]>pivot:
      right-=1
    swap(list, left,  right)

  return left  
 

def quicksort(list, left, right):
  if(left>=right): 
    return
  pivot=partition(list, left, right)
  quicksort(list, left, pivot-1)
  quicksort(list, pivot+1, right)



l=[7,12,4,34,6,9,22,45,2,1]

print l
quicksort(l, 0, len(l)-1)
print l
