# Luiza vai viajar com seus amigos e está pesquisando preços. O grupo está em dúvida entre alugar uma casa em Pipa ou em Fortaleza. 

# Caso escolham ir para Pipa, o aluguel de uma casa com 2 quartos sai por R$ 600 e o de uma com 3 quartos custa R$ 900. 
#   Lá eles pretendem fazer um passeio de barco, que custa R$ 75 por pessoa.

# Caso a escolha do grupo seja Fortaleza, eles poderão pagar R$ 950 por uma casa com 3 quartos ou R$ 1120 por uma com 4 quartos. 
#   A atração que querem visitar é um parque aquático cujo ingresso individual custa R$ 60.

# Escreva um programa que receba como entrada a quantidade de pessoas do grupo, a cidade escolhida, 
#   e a quantidade de quartos que querem na casa, e calcule e exiba o valor total da viagem, e quanto cada um irá pagar.

# Obs: Considere que todos do grupo irão para o passeio da cidade.

PIPA_VALOR_2_QUARTOS = 600
PIPA_VALOR_3_QUARTOS = 900

FORTALEZA_VALOR_3_QUARTOS = 950
FORTALEZA_VALOR_4_QUARTOS = 1120



qtd = int(input())
cidade = input().upper()
qtdQuartos = int(input())

valorViagem = 0

if cidade == "PIPA":
  valorViagem = PIPA_VALOR_2_QUARTOS if 1 <= qtdQuartos <= 2 else PIPA_VALOR_3_QUARTOS
  valorViagem += 75 * qtd

elif cidade == "FORTALEZA":
  valorViagem = FORTALEZA_VALOR_3_QUARTOS if 1 <= qtdQuartos <= 3 else FORTALEZA_VALOR_4_QUARTOS
  valorViagem += 60 * qtd

print("%.2f\n%.2f"%(valorViagem,valorViagem/qtd))

    

