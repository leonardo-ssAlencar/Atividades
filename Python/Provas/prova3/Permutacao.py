# Bob está brincando com números inteiros, ele pega um número X e permuta os dígitos desse número 
# criando assim um número Y, Bob faz isso várias vezes até que Y seja o maior possível.
# Por exemplo, se X = 690, Bob poderia criar Y's: {069, 096, 609, 690, 906, 960}; o maior deles é 960,
# então para X = 690, Bob está interessado no Y = 960.
# Sua tarefa é criar um programa para ajudar Bob, dado um X, qual o maior Y que Bob consegue criar?

# A primeira linha da entrada contém T, o número de casos de teste.
# Cada caso de teste consiste de uma linha contendo o inteiro X.

# Limites:
# 1 <= T <= 100
# 0 <= X <= 10^100

numCas = int(input())

for i in range(numCas):
  valor = input()
  lista = []
  resultado = []
  
  for m in valor: 
      lista.append(int(m))
  
  for j in range(len(lista)):
     maior = lista[0]
     for n in range(len(lista)):    
          if lista[n] > maior:
              maior = lista[n]
              
     resultado.append(maior)
     lista.remove(maior)
    
    
  print("Caso %d: "%(i+1),end="")
  for l in resultado:
    print(l, end="")
  
  print()  
  
    
