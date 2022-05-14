# Escreva um programa que solicite ao usuário:

# Sua temperatura
# Se está tendo secreção, tosse e dor no corpo (“S” ou “N”)
# Após a solicitação dos dados:

# Caso a temperatura seja maior ou igual a 37 graus e as demais respostas sejam iguais a “S”, 
#   uma mensagem “Exames Especiais” deve ser exibida.

# Caso a temperatura seja maior ou igual a 37 graus e as demais respostas sejam iguais a “N”, 
#   uma mensagem “Exames Basicos” deve ser exibida.
# Caso a temperatura seja menor do que 37 graus e não houver secreção, tosse e dor no corpo,
#   a mensagem será “Liberado”.
# Caso a temperatura seja inferior a 37 graus, mas houver dor no corpo, tosse e secreção,
#   a mensagem deve ser igual a “Exames Básicos”.
# Se, ao perguntar se o usuário está com secreção, tosse e dor no corpo, ele responder algo diferente de "S" ou "N",
#   exiba uma mensagem de erro.



temp = float(input())
opt = input().upper()


if(opt == "S" or opt == "N"): 
 if(temp >= 37):
   if(opt == "S"):
       print("Exames Especiais")
   elif(opt == "N"):
        print("Exames Basicos")   
 else:
    if(opt == "S"):
       print("Exames Basicos")   
    elif(opt == "N"):
       print("Liberado")
else:
    print("Erro")
    

