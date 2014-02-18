#include<stdio.h>


static void optionChina(){
  printf("option China selected\n");
}

static void optionPortugal(){
  printf("option Portugal selected\n"); 
}

int main(){
  int opt;
  printf("Select your option: \n");
  scanf("%d", &opt);
  switch(opt)
  {
    case 0: 
      optionPortugal();
      break;
    case 1:
      optionChina();
      break;
  }
  
  return 0;
}
