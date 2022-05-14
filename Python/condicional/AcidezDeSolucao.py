# Escreva um programa que leia o valor do índice de acidez (pH) de uma solução e informe se ela é ácida, básica ou neutra.
# A solução é ácida quando o pH é menor que 7
# A solução é básica quando o pH é maior que 7
# Caso contrário a solução é neutra


ph = float(input())

if(ph > 7):
 print("Basica")
elif(ph < 7):
 print("Acida")
else:
 print("Neutra")
 