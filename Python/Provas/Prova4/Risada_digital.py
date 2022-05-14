# primeira coisa que ela percebeu é que as consoantes não interferem no quanto as risadas digitais influenciam na transmissão
# do sentimento. A segunda coisa que ela percebeu é que as risadas digitais mais engraçadas são aquelas em que as sequências
# de vogais são iguais quando lidas na ordem natural (da esquerda para a direita) ou na ordem inversa (da direita para a
# esquerda), ignorando as consoantes. Por exemplo, “hahaha” e “huaauhahhuahau” estão entre as risadas mais engraçadas,
# enquanto “riajkjdhhihhjak” e “huehuehue” não estão entre as mais engraçadas, que vamos considerar sem graça               
        
x = int(input())

vogais = ["a", "e", "i", "o", "u"]

def eValida(risada):
    
    if len(risada) > 50:
        return False
    
    for i in risada:
        for j in vogais:
           if i == j:
               return True
               
    
def retirarConsoantes(risada):
    novaString = []
    for i in risada:
        eVogal = False
        for j in vogais:
            if i == j: 
                eVogal = True
        
        if eVogal:
            novaString.append(i)
            
    return novaString
                
def classificarRisada(risada):
   risada = retirarConsoantes(risada)            
   for i in range(len(risada)):
       if risada[i] != risada[(len(risada)-1)-i]:
           return False
    
   return True
       
for i in range(x):
    risada = input().lower()
    
    if eValida(risada):
        if classificarRisada(risada):
            print("ENGRACADA")
        else:
            print("SEM GRACA")
        
    
    else:
        print("INVALIDO")