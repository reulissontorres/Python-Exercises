"""Um Print Especial"""
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


for c in range(0, 3):
    texto = str(input(f'Mensagem {c+1}: '))
    escreva(texto)
