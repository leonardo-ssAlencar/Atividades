# E aí, preparado? Mais uma vez precisamos da sua ajuda! Depois de algumas trocas de aparelhos,
# e manutenções no prédio da informática, os teclados do IF (IFSULDEMINAS) sofreram uma brincadeira de mau gosto 
# na formatação do teclado, suas teclas estão trocadas. Como os computadores do IF são preparados 
# para receber qualquer software, desenvolva o mais rápido possível um programa que converta as frase da forma correta.

# Observação:o teclado trocara todas as teclas do teclado, por isso todos caracteres são aceitos.

param = input().split()

lista = []
for i in range(int(param[0])):
    lista.append(input().split())


for i in range(int(param[1])):
    mensagem = input()
    
    decod = []
    for j in mensagem:
        tamDec = len(decod)
        for m in lista:
            if j == m[0]:
               decod.append(m[1])
        
        if tamDec == len(decod):
            decod.append(j)
            
    for n in decod:
            print(n,end="")
    print()
    
    
