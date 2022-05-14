#include<stdio.h>


int main()
{
  int val = 20;
  char valor[val];

  scanf("%[^\n]s", valor);

  for(int i = 0; valor[i] ; i++)
  {
    if(valor[i] == ' ') 
    {
      valor[i] = '#';
    }
  }

  printf("%s", valor);

 return 0;
}