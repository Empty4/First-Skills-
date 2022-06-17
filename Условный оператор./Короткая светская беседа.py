print('Как ваше настроение?')
answer = input()
if ('хорош' in answer or 'прекрасн' in answer or 'замечат' in answer) and '?' not in answer:
    print('Отлично, у меня тоже всё хорошо :)')
elif ('плох' in answer or 'ужасн' in answer) and '?' not in answer:
    print('Ничего, скоро всё наладится')
else:
    print('Хоть я вас и не понял, надеюсь у вас всё хорошо :)')
