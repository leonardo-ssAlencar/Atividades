# Uma escola, ao divulgar a média dos seus alunos, decidiu incluir uma bolinha colorida ao lado da média. 
# A regra ficou assim:

    # notas maiores que 7, "bolinha verde";
    # notas entre 5 e 7 (inclusive), "bolinha amarela";
    # notas menores que 5, "bolinha vermelha".

# O seu programa, em Python, deve ler uma nota e classificá-la de acordo com a regra acima.


nota = float(input())

if nota > 7: print("bolinha verde")
elif 5 < nota <= 7: print("bolinha amarela")
else:print("bolinha vermelha")


