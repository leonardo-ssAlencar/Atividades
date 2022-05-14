#include<stdio.h>

int main()
{  
    int a,b,c ,e1,e2,e3;

    scanf("%d %d %d", &a,&b,&c);

    if(a > b && a > c)
    {
      e1 = a;
      if(b > c )
      {
       e2 = b;
       e3 = c;
      }
      else
      {
       e2 = c;
       e3 = b;
      }
    }
    else if(b > a && b > c)
    {
        e1 = b;
        if(a > c)
        {
          e2 = a;
          e3 = c;
        }
        else
        {
            e2 = c;
            e3 = a;
        }
    }
    else
    {
      e1 = c;
      if(a > b)
      {
          e2 = a;
          e3 = b;
      }
      else
      {
         e2 = b;
         e3 = a;
      }
    }
    

    
    printf("%d \n %d \n %d", e1,e2,e3);
    return 0;
}
