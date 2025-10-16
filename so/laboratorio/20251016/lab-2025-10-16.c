#include<stdio.h>
#include<stdlib.h>
#include<time.h>
/*
 * Scrivi un programma che allochi dinamicamente una matrice di interi n × m, 
 * la riempia con valori (es. random), 
 * la stampi in forma tabellare e liberi tutta la memoria allocata.
 */
int main(void){
  srand(time(NULL));
  int n,m;
  int **A = NULL; // puntatore di array di puntatori (puntatore di puntatori)
  printf("Inserisci n m:");
  if (scanf("%d %d", &n,&m) != 2 || n<0 || m<0){
    printf("Errore nello scanf!\n");
    return 1;
    
  }

  printf("Valori inseriti %d %d\n", n, m);

  A = malloc(n* sizeof(*A));
  if (!A){
    perror("malloc A");
    return 1;
  }
  for(int i = 0; i< n; i++){
    A[i]= malloc(m* sizeof(int)); // ho creato n array di m interi (per questo sizeof(int))
		if (!A[i]) {
			perror("malloc A[i]");
			for (int k = 0; k < i; k++) {
				free(A[k]);
			}
			free(A);
			return 1;
		}
    for (int i =0; i < n; i++){
      for (int j = 0; j < m; j++){
        A[i][j]= rand() % 100; //0....99
        printf("%d\t", A[i][j]);
      }
      printf("\n");
    }

  }
  return 0;
}
