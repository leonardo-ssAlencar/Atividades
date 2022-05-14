#Eles fizeram algumas mudanças em relação à confraternização anterior. Eles fizeram o seguinte para estimular cada um a dar o 
# máximo que pudesse: cada pessoa daria um valor igual ou inferior ao total sem ver quanto os demais dariam.
# Ao final, se calcularia o total arrecadado e quem deu o maior valor de todos receberia de volta o excedente, 
# caso a arrecadação ultrapassasse o valor da conta. Caso faltasse dinheiro, aquele funcionário que contribuiu com o menor valor, 
# deve completar com a quantia que estiver faltando.

# Para isso, nosso programa vai receber: o valor total da conta, um valor N (indicando o número de funcionários participantes da confraternização), 
# o nome e o valor pago por cada um dos N funcionários.

# Ao final, o programa deve exibir o valor da conta, o valor total arrecadado pelos funcionários, 
# o nome e a quantia de quem pagou mais,
# uma informação indicando se houve sobra (excedente) ou falta (insuficiente) e o valor correspondente. 
# E, em caso de falta, o nome de quem menos contribuiu assim como o valor que essa pessoa terá que pagar para completar o valor da conta total.

valorTotal = float(input())
qtdFunc = int(input())

nomeFunc = []
valorFunc = []


for i in range(qtdFunc):
    nomeFunc.append(input())
    valorFunc.append(float(input()))
    

totalArrecado = 0.0


maiorQueZero = False
maiorContribN = nomeFunc[0]
maiorContribV = valorFunc[0]
menorContribN = nomeFunc[0]
menorContribV = valorFunc[0]

for i in range(qtdFunc):
    totalArrecado+= valorFunc[i]
    
    if menorContribV >= valorFunc[i]:
        menorContribN = nomeFunc[i]
        menorContribV = valorFunc[i]
        
    elif valorFunc[i] >= maiorContribV:
        maiorContribN = nomeFunc[i]
        maiorContribV = valorFunc[i]
        
    if valorFunc[i] > 0: maiorQueZero = True
          
        
# if not maiorQueZero:
#     maiorContribN = nomeFunc[len(nomeFunc)-1]
#     menorContribN = nomeFunc[len(nomeFunc)-1]

print("Conta: R$ %.2f"%valorTotal)
print("Arrecadado: R$ %.2f"%totalArrecado)

if totalArrecado < valorTotal:
    diferenca = valorTotal - totalArrecado
    if maiorQueZero:
     print("%s pagou R$ %.2f"%(maiorContribN, maiorContribV))
    print("Valor insuficiente: falta R$ %.2f"%(diferenca))
    print("%s pagou R$ %.2f e precisa pagar mais R$ %.2f"%(menorContribN, menorContribV, diferenca))
    
elif totalArrecado > valorTotal:
    diferenca = totalArrecado - valorTotal
    if maiorQueZero:
      print("%s pagou R$ %.2f"%(maiorContribN, maiorContribV))
    print("Valor excedente: sobra R$ %.2f a ser devolvido a %s"%(diferenca, maiorContribN))
else:
    print("Foi arrecadado exatamente o valor da conta.")   
    

   
    
    