number = int(input())
first = 1
second = 1
if number > 1:
    print(1)
while second < number:
    firsts = second
    second += first
    first = firsts  # спс
    print(first)
