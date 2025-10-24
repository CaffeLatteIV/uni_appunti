/*
 * Definisci due versioni di una struct chiamata Data 
 * che contengano char a, int b, short c in ordine diverso.
 * Scrivi un programma che:
 *    stampi sizeof(struct Data1) e sizeof(struct Data2);
 *    aggiungi, direttive di packing (#pragma pack) e confronta di nuovo le dimensioni.
 * */
#include "stdio.h"
typedef struct Data1 {
  char a;
  int b;
  short c;
}Data1;

typedef struct Data2 {
  char a;
  short c;
  int b;
}Data2;
int main(void){
  /*le struct possono avere dimesioni diverse (pur avendo stessi elementi e stesso peso per elemento) 
   * in base a come sono state ottimizzate
   * ES:
   * allineamento a 4B (base)
   * un intero occupa 
   *
   * */
  printf("Data1 %ld Data2 %ld\n", sizeof(Data1), sizeof(Data2));
  return 0;
}
