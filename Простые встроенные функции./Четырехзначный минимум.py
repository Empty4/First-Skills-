number = int(input())
one = number % 10
two = number // 10 % 100
tree = number // 100 % 1000
four = number // 1000
if one > two > tree > four:
    print(one, two)  # а как сделать чтобы цифры были вместе?
