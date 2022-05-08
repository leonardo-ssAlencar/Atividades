#include<stdio.h>
#include<stdlib.h>
#include<time.h>

const int TAM = 5;

int main()
{
 srand(time(NULL));
 int M[TAM][TAM];
 int B[TAM][TAM];
 
 for(int i = 0; i < TAM; i++)
 {
  for(int j = 0; j < TAM*2; j++)
  {
      M[i][j] = rand()%11;
      B[i][j] = M[i][j]*2;
      if(j < TAM)
      {
        printf("%2d ", M[i][j]);
      }
      else
      {
        if(j == 5) printf(" | ");

        printf("%2d ", B[i][j-TAM]);
      }
  }
  printf("\n");
 }

 return 0;
}