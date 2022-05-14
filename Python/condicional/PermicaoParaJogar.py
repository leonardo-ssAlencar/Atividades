# Uma plataforma online oferece 4 tipos de jogos, 
# onde Cada um desses tipos de jogo tem uma faixa etária para que o jogador possa participar.

# Jogos de azar - Apostas esportivas, blackjack, roleta e afins. 21 anos ou mais
# MMORPG - Massively Multiplayer Online Role-Playing Game. 14 anos ou mais
# MOBA - Multiplayer Online Battle Arena. 10 anos ou mais
# Casual. Sem limite de idade

# Faça um programa que receba a idade do jogador e o tipo de jogo que ele deseja jogar e informe se ela pode jogar. 
 # Caso a idade do jogador caia fora do intervalo válido ou seja informado um tipo de jogo que não existe, 
 # deve ser emitida uma mensagem de erro de acordo com o que aconteceu.


idade = int(input())
tipoGame = input()
mensagem = ""

if(idade >= 0 and idade <= 130):
  if(tipoGame == "azar" or tipoGame == "mmorpg" or tipoGame == "moba" or tipoGame == "casual"):
   if(tipoGame == "azar" and idade <= 21 ):
       mensagem = "Volte daqui ha alguns anos."
   elif(tipoGame == "mmorpg" and idade <= 14):
       mensagem = "Volte daqui ha alguns anos."
   elif(tipoGame == "moba" and idade <= 10):
       mensagem = "Volte daqui ha alguns anos."
   else:
       mensagem = "Pode entrar!"
  else:
    print("Jogo invalido.")
  print(mensagem)

else:
 print("Idade invalida.")
