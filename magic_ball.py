import random
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет, друг, я магический шар, и я знаю ответ на любой твой вопрос!')
print('Я Вам не ТАРО!')
name = input('Назови своё имя и начнём: ')
print(f'Привет, {name}!')
while True:
  question = input('Задай вопрос, который тебя волнует: ')
  print(random.choice(answers))
  question_2 = input('Может хочешь спросить что-то еще? (да/нет): ')
  if question_2 == 'да':
    continue
  elif question_2 == 'нет':
    print(f'Воозвращайся {name}, если возникунут вопросы!')
    break
  else:
    print(f'Я тебя не понимаю, {name}, но мне кажется, что ты хочешь спросить что-то еще :)')
    continue
