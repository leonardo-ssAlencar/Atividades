# A editora Fronteira vende assinaturas de jornais e revistas, e seus valores estão indicados abaixo.
# Apenas esse mês, as assinaturas de revistas estão com 10% de desconto. 
# Escreva um programa que receba como entrada o nome do item desejado,
# e também a duração em anos da assinatura, e exiba o valor total a ser pago.

# Mural = 200.00
# O Coreto = 235.00
# Meu Lar = 180.00
# Sua Mesa = 230.00

n = input().upper()
anos = int(input())

valorTotal = 0
if n == "MURAL": valorTotal = 200 * anos
elif n == "O CORETO": valorTotal = 235 * anos

elif n == "MEU LAR": 
    valorTotal = (180 * anos) * 0.9
    
elif n == "SUA MESA": 
    valorTotal += (230 * anos) * 0.9
    
    

print("%.2f"%valorTotal)