"""Verificando as Primeiras Letras de um Texto"""
cid = str(input('Qual é sua cidade? ')).upper().split()
print('Sua cidade tem "Santo" no nome:')
print(cid[0] == "SANTO")
