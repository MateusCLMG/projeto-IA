from tabulate import tabulate    

tabela = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]


queen = 0   #numero de rainhas no tabuleiro ou linha atual

nextq = 0   #coluna em q a proxima rainha sera posicionada


badrows = []    #colunas ja ocupadas por alguma rainha


def diagonais(row,column):
    #cada while preenche as casas nas diagonais
    x = row
    y = column
    k = 0
    while(k < 8):
        if(not(tabela[x][y] == 1)):
            tabela[x][y] = 'X'
        if(x<7):
            x += 1
        if(y<7):
            y += 1
        k += 1
    x = row
    y = column
    k = 0

    while(k < 8):
        if(not(tabela[x][y] == 1)):
            tabela[x][y] = 'X'
        if(x>=0):
            x -= 1
        if(y<7):
            y += 1
        k += 1
    x = row
    y = column
    k = 0

    while(k < 8):
        if(not(tabela[x][y] == 1)):
            tabela[x][y] = 'X'
        if(x<7):
            x += 1
        if(y>=0):
            y -= 1
        k += 1
    x = row
    y = column
    k = 0

    while(k < 8):
        if(not(tabela[x][y] == 1)):
            tabela[x][y] = 'X'
        if(x>=0):
            x -= 1
        if(y>=0):
            y -= 1
        k += 1
    x = row
    y = column
    k = 0



while(queen <= 7):

    if(not(badrows.__contains__(nextq)) and tabela[queen][nextq] == 0): #se a coluna nao estiver ocupada
        badrows.append(nextq)           #declare como ocupada
        tabela[queen][nextq] = 1
        diagonais(queen,nextq)
        queen += 1
    nextq += 1

    if(nextq == 8):
        break



print(tabulate(tabela))



