#include<stdio.h>

int main()
{
 int valor, ePrimo = 0;
 
 scanf("%d", &valor);

 for(int i = 2; i <= (valor/2) ; i++)
 {
   if(valor%i == 0)
   {
      ePrimo = 1;
      break;
   }
 }
 if(ePrimo == 1)
     printf("Não é primo");

 else
    printf("É primo");


 printf("\n");

 return 0;
}