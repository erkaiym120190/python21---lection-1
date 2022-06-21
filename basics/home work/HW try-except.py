# Task 1

# try:
#     print()
# except:
#     print()
# else:
#     print()
# finally:
#     print()


# Task 2

# b = 10
# c = 11
 
# print(a)

# try:
#     print(a)
# except SyntaxError:
#     print('Такой переменной не существует')
# except: 
#     print("что-то пошло не так") 


# Task 3

# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(result)  


# Task 4

# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 + num2
# except:
#     print('Введите число!')
# else:
#     print(result)


# Task 5

# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     dict_[key] += 2
# except:
#     print('Нет такого ключа!')
# else:
#     print(dict_[key])


# Task 6

# list_ = [1, 4, 9, 16, 25, 36] 

# try:
#     list_[56]
# except IndexError:
#     print('Нет такого элемента!')
# else:
#     print(list_[i])


# Task 7

# В блоке try запросите у пользователя ввод его возраста age = int(input()). 
# Затем в том же блоке проверьте его возраст на совершеннолетие. 
# Если пользователь несовершеннолетний(младше 18), выбросите исключение ValueError с текстом:
# Доступ запрещён 
# Обработайте это исключение и другое исключение, 
# которое возникает при вводе текста вместо возраста, выдав сообщение:
# Введён некорректный возраст 
# Если ошибок не возникло распечатайте сообщение:
# Спасибо 
# и, наконец, распечатайте сообщение:
# До свидания! 
# вне зависимости от того, произошла ошибка или нет.

# try:
#     age = int(input())
    
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')


# Task 8

# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 / num2

# except (ValueError, TypeError):
#     print('Произошла ошибка!')

# else:
#     print(result)


# Task 9

# cash = int(input())
# if cash < 0: 
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)


# Task 10 (extra task 1)

# try:
#     inp1 = input()
#     inp2 = input()
#     print(int(inp1) + int(inp2))
# except:
#     print(inp1 + inp2)


# Task 11  (extra rask 2)

# Запросите у пользователя несколько слов и чисел, 
# поместите их в переменную inp1 введенных через пробел, затем:

# поместите эти слова в список

# переберите этот список циклом и перевидете все строки в тип данных - число

# все числа поместите в отдельный list_

# а на возникающие исключение сгенерируйте свое исключение cо строкой:

# Данный элемент не является числом! 

# inp1 = input()
# a = inp1.split(' ')
# list_ = []
# for i in a:
#     try:
#         list_.append(int(i)) 
#     except:
#         raise Exception('Данный элемент не является числом!')


# Class work task 1

# try:
#     inp1 = input()
#     inp2 = input()
#     print(int(inp1) + int(inp2))
# except:
#     print(inp1 + inp2)


# Class work task 2

# dict_ = {1: 'Бегимай', 2: 'Канатбек', 3:'Айдин', 4: 'Эркайым'}
# dict_ = {value: key for key, value in dict_.items()}
# # print(dict_)

# try:
#     username = input('Введите имя пользователя: ')
#     ID = dict_[username]
#     print(ID)
# except KeyError:
#     print('Введенного юзера нет в базе данных')
# else:
#     print(f'Добро пожаловать, {username}!')
# finally:
#     print('Спасибо!')


# Class work task 3

# try:
#     age = int(input('Сколько вам лет? '))
#     if age <= 0: 
#         raise Exception('Ваш возраст должен быть больше нуля!')
# except ValueError:
#     print('Введите число, а не строку!')

