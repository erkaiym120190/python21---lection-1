# CLASS WORK TASK 1

# with open('numbers.txt', 'w') as file1:
#     for number in range(1, 21):
#         file1.write(str(number) + '\n')

# with open('squares.txt', 'w') as file2:
#     with open('numbers.txt') as file1:
#         nums = file1.read().split('\n')
#         nums.pop()
#         nums1 = list(map(int, nums))
#         print(nums1)
#         for num in nums1:
#             file2.write(str(num**2) + '\n')


# # CLASS WORK TASK 2

# with open('username.txt', 'w') as file1:
#     while True:
#         username = input('Введите имя: ')
#         if username.lower() == 'end':
#             break
#         file1.write(f'{username} - {len(username)}\n')


# Мини-проект "Виселица"

from random import choice
pictures = (
"""
+---+
|   |
    |
    |
    |
    |
=========
""",
"""
+---+
|   |
O   |
    |
    |
    |
=========
""",
"""
+---+
|   |
O   |
|   |
    |
    |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
 =========
""",
"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
 =========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
)


max_wrong = len(pictures)

WORDS = ('питон', 'акула', 'суслик','программирование', 'жемчужина', 'лето', 'жара', 'сокол',
        'достоинство', 'сущность', 'признание', 'победа', 'выгорание', 'помощь', 'ревность',
        'глубина', 'чародейство', 'совесть', 'призвание')

word = choice(WORDS)
us_word = '_' * len(word)
wrong = 0
used = []

while wrong < max_wrong and us_word != word:
    print(pictures[wrong])
    print('\nВы использовали следующие буквы:\n', used)
    print('\nНа данный момент слово выглядит так:\n', us_word)

    guess = input('\nВведите свою букву: ')

    while guess in used:
        print('Вы уже угадали букву', guess)
        guess = input('Введите свою букву: ')
    
    used.append(guess)

    if guess in word:
        print('\nДа! \'' + guess + '\' есть в этом слове!')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += us_word[i]
        us_word = new
    else:
        print('\nИзвините, но буквы \'' + guess + '\' нет в слове.')
        wrong += 1

if wrong == max_wrong:
    # print(pictures[wrong])
    print('\nВас повесили!')
else:
    print('\nВы угадали слово!')

print('\nЗагаданное слово было \'' + word + '\'')