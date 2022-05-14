# Faça um programa que dado um número inteiro n, imprima n linhas, onde cada linha deve seguir o seguinte padrão:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# …
# nnnnnnnnnn

n = int(input())

if 1 <= n <= 30:
 n += 1
 for i in range(n):
    for j in range(i):
        print(i, end="")
    
    print()