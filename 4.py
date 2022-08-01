
x1 = int(input('Число 1:'))
x2 = int(input('Число 2:'))
x3 = int(input('Число 3:'))
if x1 == x2 == x3:
	print('3')
elif x1 == x2:
	print('2')
elif x2 == x3:
	print('2')
elif x1 == x3:
	print('2')
else:
	print('0')