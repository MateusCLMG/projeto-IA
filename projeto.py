from ast import MatchSequence
from tabulate import tabulate    

tabela = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

solutions = [[1,4,6,0,2,7,5,3],[1,4,6,3,0,7,5,2],[1,5,0,6,3,7,2,4],
[1,5,7,2,0,3,6,4],[1,6,2,5,7,4,0,3],[1,6,4,7,0,3,5,2],
[2,4,7,3,0,6,1,5],[2,5,1,4,7,0,6,3],[2,4,1,7,0,6,3,5],
[0,4,7,5,2,6,1,3],[0,5,7,2,6,3,1,4],[1,3,5,7,2,0,6,4]]

def flipVertical():
    solutionsCopy = solutions.copy()
    for i in range(12):
        x = solutionsCopy
        x.reverse()
        solutions.append(x)



flipVertical()

print(solutions)

coluna = int(input("Insira em que coluna vai a primeira rainha: "))

tabela[0][coluna] = 1       # 1 simboliza uma rainha posicionada

matchedSol = []             # String com sequencias de solutions compativeis com a primeira rainha

linhaAtual = 1

print(tabulate(tabela))

tamanhoSol = len(solutions)
print(tamanhoSol)
for i in range(tamanhoSol):         #filtra solutions por solucoes q começam com o input e coloca em matched
    print(solutions[i][0])
    if solutions[i][0] == coluna:
        matchedSol.append(solutions[i])

#//////
while not linhaAtual == 8:
    print(tabulate(matchedSol))
    x = 100                                         # valores quaisquer
    nextCasa = 100                                  #para serem substituidos
    for i in range(len(matchedSol)):                #buscando nessa lista de possiveis soluções
        distance = abs(matchedSol[i][linhaAtual] - coluna)
        print(matchedSol)
        if distance < x:                            #qual solução possui proxima casa mais proxima
            x = distance                            # X eh a menor distancia da rainha anterior para a proxima
            nextCasa = matchedSol[i][linhaAtual]             #next casa diz qual casa sera ocupada
            
    for i in range(len(matchedSol)):                #remove as soluções q nao serao mais usadas 
        try:
            if not (matchedSol[i][linhaAtual] == nextCasa):  
                matchedSol.pop(i)
        except:
            break

    #linhaAtual += 1

    if len(matchedSol) == 1:            # se nao existirem outras soluções, preenche a tabela com o caminho encontrado
        for i in range(8):
            x = matchedSol[0][i]
            tabela[i][x] = 1
        break
    #print(linhaAtual)
    tabela[linhaAtual][nextCasa] = 1
    linhaAtual += 1

    

print(tabulate(tabela))
    






