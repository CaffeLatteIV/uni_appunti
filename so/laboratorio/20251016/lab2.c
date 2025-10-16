#include<stdio.h>
#include<stdlib.h>
typedef struct Node{
  int value;
  struct Node* next;
} Node;
Node* insert_head(Node* head, int value){
  Node* tmp = (Node*) malloc(sizeof(Node));
  tmp->value = value;
  tmp->next = head;
  return tmp; 
}
void print_list(Node* head){
  if (head == NULL){
    return;
  } 
  printf("%d  ", head->value);
  print_list(head->next);
  
}
void free_list(Node* head){
  if(head == NULL){
   return; 
  }
  free_list(head->next);
  free(head);
}

int main(void){

  Node * head = NULL;
  head = insert_head(head, 1);
  head = insert_head(head, 2);
  head = insert_head(head, 3);
  head = insert_head(head, 1);
  head = insert_head(head, 3);

  print_list(head);
  free_list(head);
  return 0;
}
