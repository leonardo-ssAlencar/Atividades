#include <stdio.h>

int main(void) {
  int p[10];
  int x = 2;

  for (int i = 0; i < 10; i++) {
    p[i] = x;
    x += 2;
  }

  int v[10];
  x = 10;
  for (int i = 0; i < 10; i++) {
    v[i] = x;
    x++;
  }

  int s[10];

  for (int i = 0; i < 10; i++) {
    s[i] = p[i] + v[i];
    printf("%d + %d = %d\n", p[i], v[i], s[i]);
  }
}