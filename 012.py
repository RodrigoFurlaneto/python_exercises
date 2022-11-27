# This application will return a new product price (5% off)

old_price = float(input('Enter the product price: $'))

five_percent_off = old_price * 0.95

print('The new product price is ${:.2f}'.format(five_percent_off))
