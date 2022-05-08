#include<stdio.h>

int main()
{
 int vetor[5];
 int j = 4;
 int vetor2[5];

 for(int i = 0; i < 5; i++)
 {
     scanf("%d", &vetor[i]);
    vetor2[j] = vetor[i];
    j--;
 }
 for(int i = 0; i < 5; i++)
 {
     printf("V1: %d \t V2: %d\n", vetor[i], vetor2[i]);
     
 }

 return 0;
}