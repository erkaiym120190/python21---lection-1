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
len_word = '*' * len(word)
wrong = 0

while wrong < max_wrong and len_word != word:
    print(pictures[wrong])
    attempt = len(pictures) - wrong 
    print('\nУ вас осталось попыток:', attempt)
    print('\nНа данный момент слово выглядит так:\n', len_word)

    guess = input('\nВведите свою букву: ')


    if guess in word:
        print('\nДа! Буква \'' + guess + '\' есть в этом слове!')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += len_word[i]
        len_word = new
    else:
        print('\nИзвините, но буквы \'' + guess + '\' нет в слове.')
        wrong += 1

if wrong == max_wrong:
    print('\nПопыток больше нет! Вас повесили!')
else:
    print('\nПобеда!Вы угадали слово!')

print('\nЗагаданное слово было \'' + word + '\'')
