def showhash():
    for lin in range(0, 3):
        for col in range(0, 3):
            print(f'[{grade[lin][col]:^1}]', end='')
        print()
    print()


def get1():
    x = 0
    try:
        x = int(input("JOGADOR 1\nEscolha onde voce quer jogar: "))
        if x < 1 or x > 9:
            print('Jogada inválida.')
            exit(1)
    except:
        print('Jogada inválida.')
        exit(1)
    if x == 1 and grade[0][0] == '':
        grade[0][0] = 'X'
    elif x == 2 and grade[0][1] == '':
        grade[0][1] = 'X'
    elif x == 3 and grade[0][2] == '':
        grade[0][2] = 'X'
    elif x == 4 and grade[1][0] == '':
        grade[1][0] = 'X'
    elif x == 5 and grade[1][1] == '':
        grade[1][1] = 'X'
    elif x == 6 and grade[1][2] == '':
        grade[1][2] = 'X'
    elif x == 7 and grade[2][0] == '':
        grade[2][0] = 'X'
    elif x == 8 and grade[2][1] == '':
        grade[2][1] = 'X'
    elif x == 9 and grade[2][2] == '':
        grade[2][2] = 'X'
    else:
        print('Posição já ocupada')
        exit(1)
    showhash()
    if check(1) == 0:
        exit(0)

def get2():
    x = 0
    try:
        x = int(input("JOGADOR 2\nEscolha onde voce quer jogar: "))
        if x < 1 or x > 9:
            print('Jogada inválida.')
            exit(1)
    except:
        print('Jogada inválida.')
        exit(1)
    if x == 1 and grade[0][0] == '':
        grade[0][0] = 'O'
    elif x == 2 and grade[0][1] == '':
        grade[0][1] = 'O'
    elif x == 3 and grade[0][2] == '':
        grade[0][2] = 'O'
    elif x == 4 and grade[1][0] == '':
        grade[1][0] = 'O'
    elif x == 5 and grade[1][1] == '':
        grade[1][1] = 'O'
    elif x == 6 and grade[1][2] == '':
        grade[1][2] = 'O'
    elif x == 7 and grade[2][0] == '':
        grade[2][0] = 'O'
    elif x == 8 and grade[2][1] == '':
        grade[2][1] = 'O'
    elif x == 9 and grade[2][2] == '':
        grade[2][2] = 'O'
    else:
        print('Posição já ocupada')
        exit(1)
    showhash()
    if check(2) == 0:
        exit(0)


def check(player):
    # Checando as linhas
    if grade[0][0] == grade[0][1] == grade[0][2] and grade[0][0] != '':
        print(f'1ª LINHA FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0
    if grade[1][0] == grade[1][1] == grade[1][2] and grade[1][0] != '':
        print(f'2ª LINHA FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0
    if grade[2][0] == grade[0][1] == grade[2][2] and grade[2][0] != '':
        print(f'3ª LINHA FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0

    # Checando as colunas
    if grade[0][0] == grade[1][0] == grade[2][0] and grade[0][0] != '':
        print(f'1ª COLUNA FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0
    if grade[0][1] == grade[1][1] == grade[2][1] and grade[0][1] != '':
        print(f'2ª COLUNA FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0
    if grade[0][2] == grade[1][2] == grade[2][2] and grade[0][2] != '':
        print(f'3ª COLUNA FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0

    # Checando as diagonais
    if grade[0][0] == grade[1][1] == grade[2][2] and grade[0][0] != '':
        print(f'DIAGONAL PRINCIPAL FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0
    if grade[0][2] == grade[1][1] == grade[2][0] and grade[0][2] != '':
        print(f'DIAGONAL SECUNDÁRIA FOI FECHADA!\nJOGADOR {player} VENCEU')
        return 0


grade = [['', '', ''], ['', '', ''], ['', '', '']]

showhash()

for k in range(0, 4):
    get1()
    get2()
get1()
print('DEU VELHA!')