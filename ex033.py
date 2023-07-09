"""Maior e Menor Valores"""
n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
n3 = int(input('3° valor: '))
#Verificando quem é menor
men = n1
if n2 < n1 and n2 < n3:
    men = n2
if n3 < n1 and n3 < n2:
    men = n3
#Verificando quem é maior
mai = n1
if n2 > n1 and n2 > n3:
    mai = n2
if n3 > n1 and n3 > n2:
    mai = n3
print('Menor valor digitado:', men)
print('Maior valor digitado:', mai)