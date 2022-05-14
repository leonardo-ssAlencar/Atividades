# Escreva um programa que leia os valores (reais) dos raios de dois círculos diferentes e informe qual dos dois possui área maior ou se possuem a mesma área.
# Use pi = 3.14

raio1 = float(input())
raio2 = float(input())

if(raio1 > raio2):
    print("Primeiro circulo")
elif(raio1 < raio2):
    print("Segundo circulo")
else:
    print("Iguais")