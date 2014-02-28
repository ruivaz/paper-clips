#include<stdio.h>
#include<stdlib.h>

static void optionChina(){
  printf("option China selected\n");
}

static void optionPortugal(){
  printf("option Portugal selected\n"); 
}

static int is_little_endian(){
  int num=1;
  if(*(char*)&num==1)
    return 0;// Return False
  else 
    return 1;// Return True
}




int intersection(int *list1, int size1, int *list2, int size2, int *result) {
  int i=0, j=0, index=0;
  
  
  while(i<size1 && j<size2 ){
    if(list1[i] == list2[j]){
      result[index]=list1[i];
      i++;
      j++;
      index++;
    }
    else { 
       if(list1[i]>list2[j]){
         j++;
       }
       else {
         i++;
       }
    }
  
  }
  return index;
}

int main(){
  int list1[3] = {1,3,5};
  int list2[5] = {1,2,3,4,5};

  int result[4];
  
  int size = intersection(list1, 4, list2, 6, result);
  
  int i;


  for(i=0; i<size; i++){
    printf("%d ", result[i]);
  }

  printf("\n");  
   
  return 0;
}
