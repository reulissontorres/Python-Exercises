'''
This code calculates the discounted price of a product. It takes the original price of the product as input and applies a 5% discount to calculate the new price. The original price and the discounted price are displayed as output.
'''

price = float(input('What is the price of the product? R$'))
new_price = price - (price * 5 / 100)
print('The product that costed R${:.2f}, on promotion with a 5% discount, will now cost R${:.2f}'.format(price, new_price))
