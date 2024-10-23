# Напишите программу, которая создает два списка чисел
# и на их основе создаёт новый список.
# В новом списке каждый элемент является суммой
# соответствующих элементов входных списков.
# Программа должна делать это на основе циклов и работать со списками любой длины.
import itertools


def fills_in_the_list(list_0):
    print("Для завершения заполнения списка введите \"stop\"")
    while True:
        try:
            input_number = input("Введите число: ")
            if input_number == "stop":
                break
            else:
                list_0.append(float(input_number))
        except ValueError:
            print("Ввод нечислового значения!")
    return list_0


list_1 = []
list_2 = []
print("Заполните первый список числами.")
fills_in_the_list(list_1)
print("\nЗаполните второй список числами.")
fills_in_the_list(list_2)
print(f"\nПервый список чисел:\n{list_1}\nВторой список чисел:\n{list_2}")
new_list = [sum(i) for i in itertools.zip_longest(
    list_1, list_2, fillvalue=0)]
print(f"Новый список чисел:\n{new_list}")
