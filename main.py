# Напишите программу, которая создает два списка чисел
# и на их основе создаёт новый список.
# В новом списке каждый элемент является суммой
# соответствующих элементов входных списков.
# Программа должна делать это на основе циклов и работать со списками любой длины.
import itertools


def fills_in_the_list(list_name):
    list_with_numbers = []
    print(f"Заполните {list_name} список числами.\n"
          f"Для завершения заполнения списка введите \"stop\"")
    while True:
        input_number = input("Введите число: ")
        if input_number == "stop":
            break
        try:
            list_with_numbers.append(float(input_number))
        except ValueError:
            print("Ввод нечислового значения!")
    return list_with_numbers


list_with_numbers_1 = fills_in_the_list("первый")
list_with_numbers_2 = fills_in_the_list("второй")

print(f"\nПервый список чисел:\n{list_with_numbers_1}\nВторой список чисел:\n{list_with_numbers_2}")

new_list = [sum(i) for i in itertools.zip_longest(
    list_with_numbers_1, list_with_numbers_2, fillvalue=0)]
print(f"Новый список чисел:\n{new_list}")
