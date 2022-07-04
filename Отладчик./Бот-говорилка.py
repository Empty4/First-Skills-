print('привет! я Максим. ты говори, я хоть и кодю, но слушаю тебя)')
while ('пока' not in (tell_me := input())) or ('до свидания' not in (tell_me := input())) or (
        'чао' not in (tell_me := input())) or ('спишемся' not in (tell_me := input())):
    if '?' in tell_me:
        if 'погода' in tell_me:
            print('я думаю нормально')
        elif 'как ты' in tell_me:
            print('да я сегодня ничего не делал, прогал только и аниме смотрел')
        elif 'что прог' in tell_me:
            print('да так, проектик один, надо фронта найти...')
        else:
            print('давай потом это обсудим? лучше скажи, как твои дела?')
    elif '!' in tell_me:
        if 'люблю' in tell_me:
            print('а я тебя сильнее')
        elif 'сдох' in tell_me:
            print('что случилось?')
            tell_me = input()
            print('сил и терпения!')
    else:
        if 'вот' in tell_me:
            print('оооо, молодчинка!')
        elif 'оке' in tell_me or 'уу' in tell_me or 'привет' in tell_me:
            pass
        else:
            print('ага')
print('ага, давай)')
