'''
This code converts an amount of money from Brazilian Real (BRL) to United States Dollar (USD), based on the exchange rate. It takes the input of how much money the user has in their wallet and calculates the equivalent amount in USD.
'''

money = float(input('How much money do you have in your wallet? R$'))
dollar = money / 3.27
print('With R${:.2f} you can buy US${:.2f}'.format(money, dollar))
