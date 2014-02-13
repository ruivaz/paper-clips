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

  printList(list, size);
  //quicksort(list, 0, size-1);
  bubblesort(list, size-1);
  printList(list, size);

  return 0;
}
