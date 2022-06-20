
import random

gues_num = 0
name = input('Здравствуйте! Как вас зовут? ')

# for i in name:
#     name1 = input(f'{name}, Вы хотите со мной сыграть в игру "Угадай число"? ')
#     if  name1 == 'yes' or 'да':
#         print('Продолжаем')
#     else:
#         print('До свидания!')

number = random.randint(1, 30)
print(f'Отлично, {name}, я загадал число, которое находится между 1 и 30. У вас будет 5 попыток. Сможете угадать? ')

while gues_num < 5:
    guess = int(input('Введите число: '))
    gues_num += 1
    if guess < number:
        print('Ваше число меньше того, чем я загадал.')
    elif guess > number:
        print('Ваше число больше того, чем я загадал.')
    elif guess == number:
        print(f'Вау, {name}! Вы угадали мое число, использовав {gues_num} попыток!') 
        break
    elif guess != number:
        print(f'А вот и не угадали! Я загадал число {number}.')
        
