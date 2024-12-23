import random
digits = '0123456789'
n = int(input('Введите количество паролей для генерации: '))
lenght = int(input('Введите длину одного пароля: '))
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
q_digits = input(f'Включать ли в пароль цифры {digits}? (+/-): ')
q_lowercase_letters = input(f'Включать ли в пароль прописные буквы {lowercase_letters}? (+/-): ')
q_uppercase_letters = input(f'Включать ли в пароль строчные буквы {uppercase_letters}? (+/-):')
q_punctuation = input(f'Включать ли в пароль символы {punctuation}? (+/-): ')
q_chars = input('Включать ли в пароль неоднозначные символы? il1Lo0O? (+/-): ')
if q_digits == '+':
  chars += digits
if q_lowercase_letters == '+':
  chars += lowercase_letters
if q_uppercase_letters == '+':
  chars += uppercase_letters
if q_punctuation == '+':
  chars += punctuation
if q_chars == '-':
  for i in 'il1Lo0O':
    chars = chars.replace(i, '')
def generate_password(n, lenght, chars):
  passwords = []
  for i in range(n):
    password = ''
    for j in range(lenght):
      password += random.choice(chars)
    passwords.append(password)
  return passwords
print(generate_password(n, lenght, chars))
