var = 'Евразией'
peace = 'Остазией'
N = int(input())
for i in range(N):
    messege = input()
    if messege == 'С кем война?':
        print(var)
    elif messege == 'С кем мир?':
        print(peace)
    elif messege == 'Меняем':
        var, peace = peace, var
