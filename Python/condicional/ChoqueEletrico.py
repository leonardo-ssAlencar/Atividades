# Ao tentar colocar um Voltorb em uma piscina, Biu acabou levando um choque do trovão.
# Curioso de saber qual foi a intensidade do choque que levou ele pesquisou e descobriu que existia uma relação entre o level do voltorb e a potência de seu choque. Como descrito na tabela abaixo.
# Escreva um programa que, dado o level do voltorb, imprima de quanto foi o choque em W segundo a tabela:

# Level	Potência (em W)
# 1-20 	20 + (level)^3
# 21-40	8000 + (level - 10)^2
# 41-60	9000 + 5*level
# 61-80	9300 + 2*level
# 81-100	9500 + level


level = int(input())
potencia = 0

if level >= 1 and level <= 20:
    potencia = 20 + level**3

elif level <= 40: 
    potencia = 8000 + (level - 10)**2

elif level <= 60:
    potencia = 9000 + 5*level

elif level <= 80:
    potencia = 9300 + 2*level

elif level <= 100:
    potencia = 9500 + level

print("Potencia de : %d W" %potencia)