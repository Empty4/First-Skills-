print('Ты дибил?')
answer1 = input()
print('Ты красив?')
answer2 = input()
if answer1 == 'да' and answer2 == 'нет':
    print('Ты умён и страшен как чёрт!')
elif answer1 == 'нет' and answer2 == 'да':
    print('Ты дебил, но мордашкой вышел!')
elif answer1 == 'нет' and answer2 == 'нет':
    print('Ты дебил, так ещё и страшен как чёрт!')
elif answer1 == 'да' and answer2 == 'да':
    print('Ты умён и красив! Выходи за меня?')
else:
    print('ERROR. Not correct answer.')
