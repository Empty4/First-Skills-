sitys = set()
for i in range(int(input())):
    sitys.add(input())
sity = set(input())
if sitys&sity==set():
    print('OK')
else:
    print('TRY ANOTHER')