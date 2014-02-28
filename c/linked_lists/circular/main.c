#include<stdio.h>
#include<stdlib.h>


typedef struct node {
  struct node *next;
  int value;
} node_t;


printList(node_t *aNode){
  if(aNode==NULL)
    return;
  node_t *p= aNode;
  
  do{
    p=p->next;
    printf("%d ", p->value);
  }while(p!=aNode);
  printf("\n");
}


static void insert_order(node_t **aNode, int value){
  node_t *new_node = malloc(sizeof(node_t));
  new_node->value = value;
  
  if(*aNode==NULL){ 
    *aNode=new_node;
    (*aNode)->next=*aNode;
     return;
  }

  node_t *p   = *aNode; 
  node_t *prev = NULL;
  do{
    prev = p;
    p = p->next;
    if(prev->value <= value && p->value >= value)
      break;

    if(prev->value > p->value){
      if(prev->value < value || p->value > value)
        break;
    }
  }while(p!=*aNode);
 
  new_node->next=p;
  prev->next=new_node;
}

int main(){

  node_t *aNode=NULL;
  insert_order(&aNode, 4);
  printList(aNode);
  insert_order(&aNode, 10);
  printList(aNode);
  insert_order(&aNode, 3);
  printList(aNode);
  insert_order(&aNode, 13);
  printList(aNode);
  insert_order(&aNode, 1);
  printList(aNode);  
  insert_order(&aNode, 22);
  printList(aNode);
  insert_order(&aNode, 7);
  printList(aNode);  
  insert_order(&aNode, 2); 
  printList(aNode);
  return 0;
}
