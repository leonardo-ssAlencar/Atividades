#O professor de programação não está divulgando as notas finais dos módulos da disciplina, 
# mas ele informou que a nota final pode ser calculada a partir da média ponderada de duas outras notas: 
#  a nota da avaliação, com um peso de 70%;
#  e a média simples das notas das listas de exercícios, com um peso de 30%.
# Porém, a quantidade de listas de exercícios varia por módulo. 
# Como um bom aluno de programação, ao invés de calcular sua média manualmente, 
# você preferiu criar um programa que calcule sua nota final no módulo.

nota = float(input())

if nota < 0 or nota > 10: exit()

qtdLista = int(input())

if qtdLista < 0: exit()
valorTotalLista = 0

for i in range(qtdLista):
  valorTotalLista += float(input())


media = (( valorTotalLista/qtdLista ) * 3 + nota * 7)/(3 + 7)

print("%.2f"%media)

if 0 <= media < 3: print("RED ZONE!")
elif 3 <= media < 5: print("DA PRA RECUPERAR!")
elif 5 <= media < 7: print("QUASE LA!")
elif 7 <= media < 9: print("TA FAVORAVEL!")
elif 9 <= media: print("EXCELENTE!")