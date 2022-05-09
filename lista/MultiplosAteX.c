#include<stdio.h>

int main()
{
 // Conjunto
 int ini = 1, fim = 500;
 int valor = 1;
 
 
 for(int i = ini; valor < fim; i++)
 {

     if(valor % 2)
     {
        printf("%d \n", valor);
     }

     valor = 3 * i;
 }

 return 0;
}