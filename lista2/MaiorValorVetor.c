#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
 srand(time(NULL));
 int vetor[20];
 int maior = 0, menor = 0;
 
 
 for(int i = 0; i < 20; i++)
 {
    vetor[i] = rand()%90;
    if(i == 0)
    {
        maior = vetor[i];
        menor = vetor[i];
    }
    if(maior < vetor[i])
    {
      maior = vetor[i];
    }
    if(menor > vetor[i])
    {
        menor = vetor[i];
    }
    
    printf(" - %d", vetor[i]);
 }
 
 printf("Maior: %d\nMenor: %d", maior, menor);



 printf("\n");


  


 return 0;
}