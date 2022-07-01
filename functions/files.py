"==========================Работа с файлами============================"
# try:
#     file = open('test.txt')
#     output = file.read()
# except:
#     pass
# finally:
#     file.close()

# print(output)



"===================Объяснение Кани==================="

# file1 = open('makers.txt', 'r')
# data = file1.read()    # метод, с пом которого мы можем считать весь файл
# print(data)

# file1 = open('makers.txt', 'r')
# data = file1.readline()    # метод, который считывает файл построчно
# print(data)

# file1 = open('makers.txt', 'r')
# data = file1.readlines() # считывает сразу все строки и помещает их в список
# print(data)


file2 = open('bootcamp.txt', 'w')
print(file2.write)('This is Makers Bootcamp\n')
strings = ['One\n', 'Two\n', 'Three\n']
file2.writelines(strings)