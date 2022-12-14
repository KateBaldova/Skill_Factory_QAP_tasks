# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается
# у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
#     Преобразование введённой последовательности в список
#     Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#     Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше
# или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
# Реализуйте его также отдельной функцией.

try:
    num_list = list(map(int, (input('Введите последовательность целых чисел через пробел').split())))
except ValueError as error:
    print(error)
    print("Введённая последовательность содержит не только числа. Выход из программы")
    raise SystemExit(1)
else:
    print('Ваша последовательность:', num_list)

try:
    num = int(input('Введите целое число'))
except ValueError as error:
    print(error)
    print("Введено нечисловое значение. Выход из программы")
    raise SystemExit(1)
else:
    num_list.append(num)
    print(f'Введённое число {num} добавлено к последовательности')

num_list.sort()

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

element = num
array = num_list

# запускаем алгоритм на левой и правой границе
key_element = binary_search(array, element, 0, len(num_list))
if key_element == 0:
    print(f'Число {num} является первым в списке, индекс следующего за ним элемента: {key_element + 1}')
elif key_element == len(num_list) - 1:
    print(f'Число {num} является последним в списке, индекс предыдущего элемента: {key_element - 1}')
else:
    print(f"Индекс элемента, который меньше введенного пользователем числа: {key_element - 1}, \n"
          f"Индекс элемента, который больше или равен введенному пользователем числу: {key_element + 1}")






