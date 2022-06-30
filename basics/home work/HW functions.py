# Task 1

# def add(a, b):
#     return a + b

# print(add(2, 3))


# Task 2

# def get_string_length(a):
#     return len(a)

# print(get_string_length('hello')) 


# Task 3

# def get_type(a, b):
#     print(type(a))
#     print(type(b))
#     return 

# get_type(5, 's')


# Task 4

# def divide(a, b):
#     return a / b

# print(divide(5, 10)) 


# Task 5

# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# def dictionary(obj):
#     for keys in dict_:
#         print(keys)

# dictionary(dict_)


# Task 6

# num = 6
# def check(num):
#     if num % 2 == 0:
#         return('It is even number')
#     else:
#         return('It is odd number')

# print(check(num))


# Task 7

# def is_palindrome(word_):

#     word_ = word_.lower()
#     if word_[::-1] == word_:
#         return True
#     else:
#         return False

# print(is_palindrome('довод')) 


# Task 8

# def max_num(a, b):
#     return (max(a, b))

# print(max_num(10, 12)) 


# Task 9

# def multiply_list(nums):
#     total = 1
#     for num in nums:
#         total *= num
        
#     return total

# numbers = [1, 2, 3, 4, 5, 6]

# print(multiply_list(numbers))
    

# Task 10

# def sum_digits(num):
#     total = 0
#     for i in str(num):
#         total += int(i)
    
#     return total

# num1 = 105

# print(sum_digits(num1))def sum_digits(num):
#     total = 0
#     for i in str(num):
#         total += int(i)
    
#     return total

# num1 = 105

# print(sum_digits(num1))





# Class work task 1

# Напишите функцию get_info, которая запрашивает у пользователя имя и фамилию, 
# последовательно. Далее внутри get_info вызовите другую функцию generate_password, 
# которая будет генерировать пароль при помощи конкатенации имени и фамилии пользователя 
# и рандомных 7 чисел (в промежутке от 0 до 9). В конце функция get_info возвращает 
# пользователю сгенерированный пароль.



# def generate_password(param1, param2):
#   import random
#   random_list = random.sample(range(1, 10), k=7)
#   random_list = [str(i) for i in random_list]
#   password = param1 + param2 + ''.join(random_list)
#   return password

# def get_info(name_ = input('Введите ваше имя: '),
#             last_name = input('Введите вашу фамилию: ')):
#   password = generate_password(name_, last_name)
#   return password
              
# print(get_info())



# Class work task 2

# Напишите калькулятор на функциях. У вас должна быть основная функция get_data, 
# которая запрашивает два числа, и действие (сложение, вычитание, умножение, деление). 
# И в зависимости от выбранного действия get_data должна вызывать ту или иную функцию, 
# в которой будет прописан алгоритм выполнения действий. В конце выдается результат 
# через функцию result.

# def add(a, b):
#   return a + b
  
# def substract(a, b):
#   return a - b
  
# def multiply(a, b):
#   return a * b
  
# def division(a, b):
#   return a / b

#   def result(param):
#     return param

# def get_data(action):
#   num1 = int(input('Введите первое число: '))
#   num2 = int(input('Введите вторoе число: '))

#   dictionary = {'+': add(num1, num2), 
#                 '-': substract(num1, num2),
#                 '*': multiply(num1, num2),
#                 '/': division(num1, num2)}

#   some_result = dictionary[action]
#   return some_result

# action = input('Выберите действие из: + - * /' + '\n')
# print(get_data(action))


# Class work task 3

# Напишите функцию, которая будет принимать 2 обязательных параметра: 
# вкус мороженого и размер. И также функция может принимать необязательные параметры, 
# которые могут выступать в качестве топпинга к мороженому. Выдайте результат
  
# def make_icecream(name, size, **kwargs):
#   print(f'Your {name} icecream {size} size')

#   if kwargs:
#     print('Your toppings: ')
#     for value in kwargs.values():
#       print(value)

# make_icecream(name='chocolate', size='medium',
#               topping1='peanuts', topping2='coconut')
  
  