#include<stdio.h>
#include<stdlib.h>
#include<time.h>

const int TAM = 5;

int main()
{
 srand(time(NULL));
 int M[TAM][TAM];
 int pos[3];
 for(int i = 0; i < TAM; i++)
 {
  for(int j = 0; j < TAM*2; j++)
  {
      M[i][j] = rand()%11;
      
      
  }
  printf("\n");
 }

 return 0;
}