#include<stdio.h>
#include<stdlib.h>

static int *merge(int *left, int *right, int left_size, int right_size);

static void swap(int *list, int index1, int index2){
  int temp=list[index1];
  list[index1]=list[index2];
  list[index2]=temp;
}

static int partition(int *list, int start, int end){
  int pivot = list[start];
  
  while(start<end){
    while(list[start]<pivot) 
      start++;
    while(list[end]>pivot) 
      end--;
    swap(list, start, end);
  }
  
  return start;
    
}

void quicksort(int *list, int start, int end){
  if (start>=end) 
    return;
  int pivotIndex = partition(list, start, end); 
  quicksort(list, start, pivotIndex-1);
  quicksort(list, pivotIndex+1, end);
}

void bubblesort(int *list, int size){
  int swaps=1;
  int i;
  while(swaps){
    swaps=0;
    for(i=0; i<size-1; i++){
      if(list[i]>list[i+1])
        swap(list, i, i+1);
        swaps=1;
    }
    size--;
  }
}


static int *partitionList(int *list, int beginIndex, int endIndex){
  int size=(endIndex-beginIndex) + 1;
  int *resultList = malloc(sizeof(int)*size);
  int i;

  for(i=0; i<=size; i++){
    resultList[i] = list[beginIndex+i];
  }

  return resultList;
}

int *mergeSort(int *list, int size){
  if (size <= 1)
    return list;
  int mid = (size - 1)/2;
  int *left  = partitionList(list, 0, mid); 
  int *right = partitionList(list, mid+1, size);
  left = mergeSort(left, mid+1);
  right = mergeSort(right, size-(mid+1));
  return merge(left, right, mid+1, size-(mid+1));
}



static int *merge(int *left, int *right, int left_size, int right_size){
  int *merge_list=malloc(sizeof(int)*(left_size+right_size));
  int left_index, right_index, i;
  left_index = right_index = i = 0;
  
  while (left_index<left_size || right_index<right_size){
    if(left_index<left_size && right_index<right_size){
      if(left[left_index]<right[right_index]){
        merge_list[i]=left[left_index];
        left_index++;
        i++;
      }
      else{
        merge_list[i]=right[right_index];
        right_index++;
        i++;
      }
    }
    else if(left_index<left_size){
      merge_list[i]=left[left_index];
      left_index++;
      i++;
    }
    else {
      merge_list[i]=right[right_index];
      right_index++;
      i++;
    }
  }
  free(right);
  free(left);
  return merge_list;
}

