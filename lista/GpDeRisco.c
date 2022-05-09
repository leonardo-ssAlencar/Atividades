#include <stdio.h>

int main()
{
 int idade, gpRisco = 9;
 float peso;
 
 scanf("%d %f",&idade,&peso);

 if(idade < 20)
 {
    if(peso > 60)
        gpRisco = (peso > 60 && peso <= 90)? gpRisco - 1 : gpRisco - 2;
    
 }
 else if(idade < 50)
 {
    gpRisco -= 3;
    if(peso > 60)
        gpRisco = (peso > 60 && peso <= 90)? gpRisco - 1 : gpRisco - 2;
 }
 else
 {

    gpRisco -= 6;
    printf("%d \n\n", gpRisco);
    if(peso > 60)
        gpRisco = (peso > 60 && peso <= 90)? gpRisco - 1 : gpRisco - 2;
 }
   
   printf("Grupo de risco: %d \n", gpRisco);
 return 0;
}