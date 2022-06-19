password1 = input()
password2 = input()
if len(password1) < 8:
    print('Короткий!')
elif len(password1) > 8 and password1 != password2:
    print('Различаются.')
elif len(password1) > 8 and password1 == password2 and '123' in password1:
    print('Простой!')
else:
    print('OK')
