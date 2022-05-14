# Alguns professores do DCX adoram tomar café e decidiram adquirir uma cafeteira especial para a sala do Departamento.
# A cafeteira utiliza cápsulas de café de vários sabores para preparar a bebida, e cada cápsula prepara o equivalente
# a duas xícaras.

# As cápsulas são vendidas em caixas pequenas (10 unidades) ou grandes (16 unidades), e ficou acertado que cada professor 
# faria a doação de quantas caixas quisesse para o grupo.

# Escreva um programa que receba como entrada a quantidade e o tamanho das caixas doadas por cada um dos sete professores
# que compartilham a cafeteira, e exiba a quantidade total de cápsulas de café doadas, e quantas xícaras cada professor 
# poderá beber.

QTD_PROF = 7
CX_PEQUENA = 10
CX_GRANDE = 16

totalDeCapsulas = 0

for i in range(QTD_PROF):
 qtdCaixas = int(input())
 tamCaixa = input()
 
 if tamCaixa.upper() == "P":
     totalDeCapsulas += (qtdCaixas * CX_PEQUENA)
 
 elif tamCaixa.upper() == "G":
     totalDeCapsulas += (qtdCaixas * CX_GRANDE)
 
 
print(totalDeCapsulas)    
print("%d"%(totalDeCapsulas/QTD_PROF)*2)
 
 
    

