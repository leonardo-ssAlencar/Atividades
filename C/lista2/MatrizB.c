#include<stdio.h>

#define TAM 10

int main()
{
 int matriz[TAM][TAM];

 for(int i = 0; i < TAM; i++)
 {
     for(int j = 0; j < TAM; j++)
     {
       matriz[i][j] = (i == j)? 1 : 0;
       
       printf("%d ", matriz[i][j]);
     }
     printf("\n");
     
 }

  
 

 return 0;  
}