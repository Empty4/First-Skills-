M = int(input())
N = int(input())
englishs = set()
germans = set()
for i in range(M):
    english = input()
    englishs.add(english)
for i in range(N):
    german = input()
    germans.add(german)
if englishs & germans == set():
    print('NO')
else:
    print(len(englishs ^ germans))
