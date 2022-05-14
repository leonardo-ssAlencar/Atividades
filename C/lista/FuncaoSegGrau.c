#include<stdio.h>
#include<math.h>

int main()
{
 int a, b, c;
 
 scanf("%d %d %d", &a,&b,&c);
 
 double delta = (double) pow(b,2)-4*a*c;
 double x1 = 0, x2 = 0;

 if(delta > 0)
 {
   x1 = (-b + sqrt(delta)) /2*a;
   x2 = (-b - sqrt(delta)) /2*a;
 }
 else if (delta == 0)
 {
   x1 = -b/(2*a);
   x2 = x1;
 }
 else
 {
    printf("Não existe raizes reais\n");
 }
 
 printf("x1 = %.2f \nx2 = %.2f ", x1, x2);

 return 0;
}