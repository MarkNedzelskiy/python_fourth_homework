# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

first_list_n = int(input("Введите длину первого списка: "))
second_list_n = int(input("Введите длину второго списка: "))

list1 = []
list2 = []

for i in range(first_list_n):
    list1.append(int(input(f"Введите {i+1} число первого списка: ")))

for i in range(second_list_n):
    list2.append(int(input(f"Введите {i+1} число второго списка: ")))

print(sorted(set(list1).intersection(list2)))