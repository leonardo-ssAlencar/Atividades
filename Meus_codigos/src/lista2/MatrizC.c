#include<stdio.h>
#include<stdlib.h>
#include<time.h>

const int TAM = 5;

int main()
{
 srand(time(NULL));
 int M[TAM][TAM];
 int pos[3] = {0, 0,0};
 for(int i = 0; i < TAM; i++)
 {
  for(int j = 0; j < TAM*2; j++)
  {
      M[i][j] = rand()%201;
      printf("%d ", M[i][j]);

      if(M[i][j] > pos[0])
      {
          pos[0] = M[i][j];
          pos[1] = i + 1;
          pos[2] = j + 1;
      }
  }
  printf("\n");
 }

 printf("O maior valor %d esta na posicao %d x %d", pos[0], pos[1], pos[2]);


 return 0;
}