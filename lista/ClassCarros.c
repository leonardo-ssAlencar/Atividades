#include<stdio.h>

int main()
{
 char sn;
 int ano, maisNovo = 0, i=0;
 float velocidade, maisRapido = 0, velTotal=0;


 for(i = 0; ; i++)
 {
   sn = getchar();
   
   if (sn == 'n') break;

   scanf("%d %f", &ano, &velocidade);

   if(ano > maisNovo)
   {
       maisNovo = ano;
   }
   if(velocidade > maisRapido)
   {
       maisRapido = velocidade;
   }
   velTotal += velocidade;   
 }

 printf("%.2f\n%d\n%.2f",maisRapido, maisNovo, velTotal/i);

 return 0;
}