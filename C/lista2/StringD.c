#include<stdio.h>

/* Digitar um texto e contar a quantidade de vezes que uma letra aparece */

int main()
{
 char texto[100], letra[1];
 
 scanf("%[^\n]s", texto); 
 
 scanf("%c", letra);

 printf("Digite uma letra: ");
 scanf("%c", letra);

 printf("texto: %s\nLetra: %c\n\n", texto, letra[0]);
 int cont = 0;
 for(int i = 0; texto[i] != '\0'; i++)
 {
     if(texto[i] == letra[0])
     {
       cont++;
     }
 }
 
 printf("A letra %c aparece %d vezes.", letra[0], cont);


 return 0;
}