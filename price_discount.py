def discount(price, rate):
	final_price = price * rate
	return final_price

old_price = float(input('please entrer prices: '))
rate = float(input('please entrer rate: '))
result = discount(old_price, rate)
print('new_price is: ' + bytes(result))
