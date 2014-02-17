#include <stdio.h>
#include "sort.h"


void printList(int *list, int size){
  int i;
  for (i=0; i<size; i++){
    printf("%d ", list[i]);
  }
  printf("\n");
}

int main(){
  
  int list[8]={11,14,4,2,45,23,3,99};

  int size=sizeof(list)/sizeof(int);

  //quicksort(list, 0, size-1);
  //bubblesort(list, size-1);
  
  printList(list, size);
  
  //merge test
  
  //int left[4]={3,7,9,14};
  //int right[3]={1,10,11};
  //int *result =  merge(left, right, 4, 3);

  int *result = mergeSort(list, 8);

  printList(result, 8);

  return 0;
}
