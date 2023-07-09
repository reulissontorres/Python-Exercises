"""Pirmeira e Última Ocorrência de uma String"""
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Na frase tem {frase.count("A")} letras "A"')
print(f'A primeira letra "A" está na posição {frase.find("A")+1}')
print(f'A letra "A" aparece pela última vez na posição {frase.rfind("A")+1}')
