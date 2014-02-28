#include<stdio.h>
#include<stdlib.h>


typedef struct node{
  int value;
  struct node *next;
} node_t;


static void insert(node_t **head, int value){
  node_t *new_node = malloc(sizeof(node_t));
  new_node->value=value;
  
  if(*head==NULL){
    *head=new_node;
    return;
  }
  
  new_node->next=*head;
  *head=new_node;
}

//Removes first ocurrence of node with value equal to value param
static int remove_node(node_t **head, int value){
  int found=0;
  if(head==NULL)
    return;

  node_t *p    = *head;
  node_t *prev = NULL;

  if(p->value==value){
    prev=*head;
    *head=(*head)->next;
    free(prev);
    return;
  }

  while(p!=NULL){
    if(p->value==value){
      prev->next = p->next;
      free(p);
      return found;
    }
    prev=p;
    p=p->next;
  }

  return found;  
}

static void printList(node_t *head){
  while(head!=NULL){
    printf("%d ",head->value);
    head=head->next;
  }
  printf("\n");
}

int main(){
 node_t *head=NULL;
 printList(head);
 insert(&head, 4);
 printList(head);
 insert(&head, 6);
 printList(head);
 insert(&head, 11);
 printList(head);
 insert(&head, 19);
 printList(head);
 remove_node(&head, 19);
 printList(head);

 return 0;    
}
