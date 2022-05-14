#include<stdio.h>

/* Receber um nome e imprimir os caracteres nas
posições impares.*/

int main()
{
 char nome[20];
 scanf("%s[^\n]", nome);
 int i = 0;
 while(nome[i] != '\0')
 {
  if(i % 2 == 0)
    printf("%c\n", nome[i]);

  i++;
 }
 
}