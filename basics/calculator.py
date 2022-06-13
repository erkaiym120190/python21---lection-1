num = float(input('Введите первое число: '))
num1 = float(input('Введите второе число: '))
sum = input('Введите действие: ')

if sum == '+':
    result = num + num1
    print(result)
elif sum == '-':
    result = num - num1
    print(result)
elif sum == '*':
    result = num * num1
    print(result)
elif sum == '/':
    result = num / num1
    print(result)
elif sum == '%':
    result = num % num1
    print(result)
elif sum == '**':
    result = num ** num1
    print(result)
elif sum == '//':
    result = num // num1
    print(result)
elif num1 == 0:
    print('Деление на 0!')
else:
    print('Данной операции нет в системе')


