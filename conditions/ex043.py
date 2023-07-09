"""Índice de Massa Corporal"""
peso = float(input('Seu peso (Kg): '))
alt = float(input('Sua altura (m): '))
imc = peso / alt ** 2
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[4;31mAbaixo do peso\033[m')
elif 18.5 <= imc < 25:
    print('\033[4;32mPeso ideal\033[m')
elif 25 <= imc < 30:
    print('\033[4;33mSobrepeso\033[m')
elif 30 <=imc < 40:
    print('\033[4;33mObesidade\033[m')
elif imc >=40:
    print('\033[4;31mObesidade mórbida\033[m')
