way = input('Вы желаете шифровать или дешифровать текст? (ш/д): ')
while way not in ['ш', 'д']:
  print('Введите ш - шифрование, д - дешифрование')
  way = input('Вы желаете шифровать или дешифровать текст? (ш/д): ')
lng = input('Введите язык (ru/en): ')
while lng not in ['ru', 'en']:
  print('Введите корректный язык')
  lng = input('Введите язык (ru/en): ')
step = input('Введите шаг сдвига: ')
while not step.isdigit():
  print('Введите корректное значение!')
  step = input('Введите шаг сдвига: ')
text = input('Введите текст: ')

if lng == 'ru':
  total_1 = 1071
  total_2 = 1103
  total_3 = 1040
  total_4 = 1072
else:
  total_1 = 90
  total_2 = 122
  total_3 = 65
  total_4 = 97
if way == 'ш':
  for i in text:
    if i.isalpha():
      if i.isupper():
        if ord(i) + int(step) > total_1:
          print(chr(ord(i) + int(step) - 32), end = '')
        else:
          print(chr(ord(i) + int(step)), end = '')
      else:
        if ord(i) + int(step) > total_2:
          print(chr(ord(i) + int(step) - 32), end = '')
        else:
          print(chr(ord(i) + int(step)), end = '')
    else:
      print(i, end = '')
else:
  for i in text:
    if i.isalpha():
      if i.isupper():
        if ord(i) - int(step) < total_3:
          print(chr(ord(i) - int(step) + 26), end = '')
        else:
          print(chr(ord(i) - int(step)), end = '')
      else:
        if ord(i) - int(step) < total_4:
          print(chr(ord(i) - int(step) + 26), end = '')
        else:
          print(chr(ord(i) - int(step)), end = '')
    else:
      print(i, end = '')
