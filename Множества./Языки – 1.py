M = int(input())
N = int(input())
for i in range(M+N):
    one_language = set()
    one_language.add(input())
if (len(one_language)-((M+N)-len(one_language)))*-1 == 0:
    print('NO')
else:
    print((len(one_language)-((M+N)-len(one_language)))*-1)