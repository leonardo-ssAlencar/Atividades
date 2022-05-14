# José está prestes a inaugurar seu supermercado. 
#   Ele acredita que o cidadão brasileiro é capaz de pagar suas compras sozinho, 
#   sem precisar de um funcionário para conferir se o que ele está pagando corresponde aos produtos que ele está levando. 

# Para isso ele vai precisar de um programa que irá ler o dia da semana, o preço do produto, 
#   a opção do produto ("prata" ou "ouro") e o nome. 

# Se a compra estiver sendo realizada na segunda, terça ou quarta e a opção do produto for "ouro", 
#   o preço do produto ficará pela metade. 

# Se a compra estiver sendo realizada na quinta ou sexta e o preço estiver entre R$ 10.00 e R$ 100.00, 
#   o preço será reduzido para um terço do valor original.

# Se a compra estiver sendo realizada no sábado e a opção for prata, o preço do produto será o triplo.
# Em qualquer outro caso, o preço será o dobro.

dia = input()
preco = float(input())
opcao = input()
nome = input()

precoFinal = 0.0

if(dia == "seg" or dia == "ter" or dia == "qua"):
    if(opcao == "ouro"):
      precoFinal = preco/2
    else:
      precoFinal = preco * 2
      
elif(dia == "qui" or dia == "sex"):
    if(preco >= 10 and preco <= 100):
        precoFinal = 1/3 * preco
    else:
        precoFinal = preco * 2

elif(dia == "sab"):
    if(opcao == "prata"):
        precoFinal = preco*3
    else:
        precoFinal = preco * 2

else:
    precoFinal = preco * 2



print("O preco do produto %s no dia %s eh %.2f"%(nome,dia,precoFinal))