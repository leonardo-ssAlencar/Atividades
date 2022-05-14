# Luíz Carlos é um carteiro muito comprometido com seu trabalho. Ele participou de uma reunião recente em 
# que foi informado de que deveria entregar pelo menos 100 correspondências por dia para dar conta do grande 
# fluxo de envios na época de Natal.

# Escreva um programa que receba como entrada a quantidade de correspondências entregues por ele em cada um dos
# sete dias da semana, e exiba em quantos dias ele cumpriu a meta, e a média de entregas diárias que ele fez no período.

total = 0
qtdAtingiuMeta = 0


for i in range(7):
  qtdCartasEntr = int(input())
  
  if qtdCartasEntr >= 100:
      qtdAtingiuMeta+=1
  
  total += qtdCartasEntr
  
print(qtdAtingiuMeta)  
print(total/7)

