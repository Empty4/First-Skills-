password1 = input()
password2 = input()
if len(password1) < 8 or password1 != password2:
    print('Короткий')
else:
    print('OK')
