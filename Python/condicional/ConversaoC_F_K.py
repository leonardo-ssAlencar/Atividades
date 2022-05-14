# Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.

# Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
# Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
# Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius


escala = input()
valor = float(input())


if(escala == "F"):
 if (valor >= -459.67):
   print("%.2f C"%(((valor - 32)/9)*5))
   print("%.2f K"%( (valor - 32)* 5/9 + 273.15))
 else:
    print("Valor de temperatura abaixo do minimo")

elif(escala == "K"):
  if(valor >= 0.0):
    print("%.2f C"%( (valor - 273.15)) )
    print("%.2f F"%( (valor - 273.15) * 9/5 + 32) )
    
  else:
    print("Valor de temperatura abaixo do minimo")

elif(escala == "C"):
  if(valor >= -273):
    print("%.2f F"%( (valor * 9/5 + 32) ))
    print("%.2f K"%(valor + 273.15))
  else:
    print("Valor de temperatura abaixo do minimo")