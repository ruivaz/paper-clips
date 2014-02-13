#include<stdio.h>

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
