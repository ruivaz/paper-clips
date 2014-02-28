#include<stdio.h>
#include<string.h>
int main(){
  
  int i;
  char msg[9];
  for(i=1; i<101; i++){
    msg[0]='\0';
    if (i%3==0)
      strcat(msg, "Fizz");
    if (i%5==0)
      strcat(msg, "Buzz");

    msg[0]=='\0'? printf("%d\n",i) : printf("%s\n",msg); 

  }
  
  return 0;
}
