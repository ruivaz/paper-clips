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



def mergeSort(list):
  size = len(list)
  if size<=1:
    return list 
  mid = size/2
  left=list[0:mid]
  right=list[mid:size]
  #print left
  #print right

  left=mergeSort(left)
  right=mergeSort(right)
  return merge(left, right, len(left), len(right))
   

def merge(left, right, leftSize, rightSize):
  leftIndex=0
  rightIndex=0
  resultList = []
  while rightIndex < rightSize or leftIndex < leftSize:
    if rightIndex < rightSize and leftIndex < leftSize:
      if left[leftIndex] <= right[rightIndex]:
        resultList.append(left[leftIndex])
        leftIndex+=1
      else:
        resultList.append(right[rightIndex])
        rightIndex+=1
    elif rightIndex < rightSize:
      resultList.append(right[rightIndex])
      rightIndex+=1
    else:
      resultList.append(left[leftIndex])
      leftIndex+=1
  return resultList

      

l=[7,12,4,34,6,9,22,45,2,1]

l1=[11,15,23,24,32]
l2=[9,32,42,44,54,81]
#print l
#quicksort(l, 0, len(l)-1)

print mergeSort(l)
