sistem = 500
print(sistem)
number_lower = 1
number_up = 1000
while (no := input()) != '=':
    if no == '>':
        number_lower = sistem
        sistem += (number_up - number_lower) // 2
    elif no == '<':
        number_up = sistem
        sistem -= (sistem - number_lower) // 2
    print(sistem)
print(sistem)
