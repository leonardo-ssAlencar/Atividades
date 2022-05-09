#include<stdio.h>
#include<stdlib.h>
#include<time.h>

const int tam = 50;

int main()
{
 srand(time(NULL));
 int lancamentos[tam];
 int ocoSeis = 0;

 for(int i = 0; i < tam; i++)
 {
    lancamentos[i] = rand()%7;
    if (lancamentos[i] == 6)
    {
        ocoSeis++;
    }
    printf(" - %d", lancamentos[i]);
 }
 double perc = (double) ocoSeis/tam;
 printf("\n percentual de ocorrencia de 6: %.3lf",perc*100);

 return 0;
}