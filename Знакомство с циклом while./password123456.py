password1 = input()
password2 = input()
if len(password1) < 8:
    print('Короткий!')
elif password1 != password2:
    print('Различаются.')
elif '123' in password1:
    print('Простой!')
else:
    print('OK')
