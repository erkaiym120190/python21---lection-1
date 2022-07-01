"==============List================"
# списки - изменяемый, индексиремый, упорядоченный, итерируемый тип данных, 
# предназначенный для хранения любых данных в определенном порядке

list_ = [1, 2, 4, 'hello', [0.1, 2], {"a":3}]
list_[1] # 2
list_[4] # [0.1, 2]
list_[4][0] # 0.1
list_[3][0] # 'h'
list_[-1]["a"] # 3


"=========Создание списков==========="
list1 = [1,2,3]
list2 = list('hello') # ['h','e','l','l','o']
list3 = list(range(1,11)) # [1,2,3,4,5,6,7,8,9,10]
list4 = [1] * 5 # [1,1,1,1,1]

"==========Методы списков==========="
# append добавляет элемент в конец списка
list_ = []
list_.append(1)
print(list_) # [1]
list_.append("hello")
print(list_) # [1, "hello"]
list_.append([1,2,3,4]) 
print(list_) # [1, "hello", [1,2,3,4]]
list_.append(1,2,3) # TypeError: append() takes exactly one argument (3 given)

# clear очищает список
list_.clear()
print(list_) # []

# count считает количество принятого элемента в списке
list_ = [1,2,1,4,1,5,1,7,2,4,4]
list_.count(1) # 4
list_.count(2) # 2
list_.count(4) # 3

list_ = ['hello', 'hello', 'hello']
list_.count('h') # 0
list_.count('hello') # 3
len(list_) # 3

# len считает количество обьектов в списке
list_ = [1, 2, [3, 4, 5], 6, 7, [8, 9, 10]]
len(list_) # 6

# extend добавляет элементы второго списка в первый, изменяя первый
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1) # [1,2,3,4,5,6]
print(list2) # [4,5,6]

# index возвращает индекс первого вхождения принятого элемента
list1 = [1,2,3,4,1,2,3,5,4,1]
list1.index(3) # 2
list1.index(1) # 0

# insert добавляет элемент по индексу list.insert(index, obj)
list_ = [1,2,3]
list_.insert(0, "hello")
print(list_) # ["hello", 1, 2, 3]
list_.insert(2, 10) 
print(list_) # ["hello", 1, 10, 2, 3]
list_.insert(100, "bye")
print(list_) # ["hello", 1, 10, 2, 3, "bye"]

# pop удаляет элемент из списка по индексу и результатом отработанного метода будет удалененый элемент
list_ = [1,2,3,4,5,6,7]
popped = list_.pop()
print(list_, popped) # [1,2,3,4,5,6]  7
popped = list_.pop(1)
print(list_, popped) # [1,3,4,5,6]  2

# remove удаляет первый принятый элемент в списке
list_ = [1,2,34,1,2,3,1,2,4,1,2,6]
list_.remove(2)
print(list_) # [1, 3, 1, 2, 3, 1, 2, 4, 1, 2, 6]
print(str(list_))

# reverse изменяет список, расставляя его элементы в обратном порядке
list_ = [1,2,3,4,5]
list_.reverse()
print(list_) # [5,4,3,2,1]
new_list = list_[::-1] # [1,2,3,4,5]

# sort сортирует список, состоящий из элементов одного типа данных в возрастающем порядке (алфавитном для строк)
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort()
print(list_) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = ['a', 'c', 'd', 'b', 'f', 'e', 'A', 'C', 'B']
list_.sort()
print(list_) # ['A', 'B', 'C', 'a', 'b', 'c', 'd', 'e', 'f']

list_ = [1,2,3,'hello'] # TypeError: '<' not supported between instances of 'str' and 'int'
list_.sort()

# reverse=True сортирует по убыванию
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort(reverse=True) # [10,9,8,7,6,5,4,3,2,1]


# Методы списков

# list.append() - добавляет элемент в конец списка
# list.extend() - добавляет элементы второго списка в первый, изменяя первый
# list.insert() - добавляет элемент по индексу list.insert(index, obj)
# list.remove() - удаляет первый принятый элемент в списке
# list.pop() - удаляет элемент из списка по индексу и результатом отработанного метода будет удалененый элемент
# list.index() - возвращает индекс первого вхождения заданного элемента
# list.count() - возвращает количество элементов со значением x
# list.sort() - сортирует список на основе функции
# list.reverse() - разворачивает список
# list.copy() - поверхностная копия списка
# list.clear() - очищает список


# list.append() - добавляет элемент в конец списка
# list.extend() - добавляет элементы второго списка в первый, изменяя первый
# list.insert() - добавляет элемент по индексу, list.insert(ind, obj)
# list.remove() - удаляет первый принятый элемент в списке
# list.pop() - удаляет элемент из списка по заданному индексу и результатом 
# отработанного метода будет удаленный элемент
# list.index() - возвращает индекс первого вхождения заданного элемента
# list.count() - возвращает количество элементов с заданным значением х
# list.sort() - сортирует список, состоящий из элементов одного типа данных в возрастающем порядке (алфавитном для строк)
# list.reverse() - разворачивает список
# list.copy() - создает копию списка
# list.clear() - очищает список

# list.append() - добавляет элемент в конец списка
# list.clear() - очищает список
# list.copy() - создает копию списка
# list.pop() - удаляет заданный элемент и результатом отработанного метода будет заданный элемент
# list.count() - возвращает количество заданных элементов х
# list.extend() - добавляет элементы второго списка в первый, изменяя первый список
# list.insert() - добавляет элементы по индексу (index, obj)
# list.reverse() - разворачивает список
# list.sort() - сортирует список, состоящий из элементов одного типа данных
# list.remove() - удаляет первый принятый элемент в списке
# list.index() - возвращает индекс первого вхождения заданного элемента





# append - добавляет элемент в конец списка
# copy - создает копию списка
# pop - удаляет заданный элемент и возвращает его
# clear - очищает список
# reverse - разворачивает список
# extend - добавляет элементы второго списка в первый, изменяя первый
# insert - добавляет новый элемент по индексу(index, obj)
# remove - удаляет новый принятый элемент в списке
# index - возвращает индекс первого вхождения заданного элемента
# sort - сортирует список одного типа данных
# count - возвращает количество заданного элемента х













