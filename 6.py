
password1 = input('Введите пароль')
password2 = input('Введите пароль еще раз')
a = 0
while a == 0:
	if len(password1) < 8:
		print('Нехватает символов')
		password1 = input('Введите пароль')
		password2 = input('Введите пароль еще раз')
	elif '123' in password1:
		print('Простой пароль')
		password1 = input('Введите пароль')
		password2 = input('Введите пароль еще раз')
	elif password1 != password2:
		print('Ваши пароли не совпадают')
		password1 = input('Введите пароль')
		password2 = input('Введите пароль еще раз')
	else:
		a = 1
		print('OK')