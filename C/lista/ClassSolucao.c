#include<stdio.h>

int main()
{
 float x;
 do
 {
  scanf("%f",&x);
  if(x > 0)
  {
    if(x > 7)
    {
      printf("BASICA");
    }
    else if(x < 7)
    {
      printf("ACIDA");
    }
    else
    {
      printf("BASICA");
    }
  }
  printf("\n");
 } 
 while (x != -1);
    


 return 0;
}