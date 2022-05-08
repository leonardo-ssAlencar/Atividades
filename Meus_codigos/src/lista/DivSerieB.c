#include <stdio.h>

int main()
{
 double h = .0;
 int cont = 1;
 for(int i = 1; i <= 50; i++)
 {
   printf("%d / %d\n", cont, i);
   h += (double) cont/i;
   cont += 2;
 }

 printf("\n\nResultado: %.4lf \n\n", h);

}