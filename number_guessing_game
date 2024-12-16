print('Добро пожаловать в числовую угадайку!')
def number_guessing_game(right):
  import random
  num = random.randint(1,right)
  count = 0
  
  def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= right:
      return True
    else:
     return False
  while True:
    count += 1
    n = input(f'Введите число от 1 до {right}:')
    if is_valid(n):
      n = int(n)
    else:
      print(f'А может быть все-таки введем целое число от 1 до {right}?')
      continue
    
    if n < num:
      print('Ваше число меньше загаданного, попробуйте еще разок')
    elif n > num:
      print('Ваше число больше загаданного, попробуйте еще разок')
    else:
      print(f'Вы угадали, поздравляем! Количество попыток {count}!')
      print('Спасибо, что играли в числовую угадайку.')
      q = input('Сыграем еще раз? (да/нет)')
      if q == 'да':
        number_guessing_game(int(input('Введите правую границу:')))
      else:
        break
number_guessing_game(int(input('Введите правую границу:')))
