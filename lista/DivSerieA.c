#include<stdio.h>

int main()
{
 double h=0;
 int qtd;

 scanf("%d", &qtd);

 for(int i = 2; i <= qtd; i++)
 {
  h += (double)1/i;
 }

 printf("O valor de H é %.5lf", h+1);
 return 0;
 
}