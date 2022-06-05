nick = input()
password = input()
if '@' not in nick and '@' in password:
    print('ОК')
else:
    print('ERROR')