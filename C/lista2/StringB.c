#include<stdio.h>

/* Ler uma string colocar em caixa alta e imprimir ela invertida */

void upper(char *nome);

int main()
{
 char nome[30];

 scanf("%s[^\n]", nome);
 
 upper(nome);
 int cont =0;
 while(nome[cont])
  {
      cont++;
  }

  for(int i = cont; i >= 0; i--)
  {
    printf("%c\n", nome[i]);
  }
 

 return 0;
}


void upper(char *nome)
{
 for(int i = 0; *nome; i++)
 {
  if(*nome > 90)
  {
      *nome -= 32;
  }

  nome++;
 }
}