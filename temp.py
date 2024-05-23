# import inspect


# def print_call_stack():
#     # Функция inspect.stack() возвращает объект-генератор.
#     # В каждом элементе генератора хранится именованный кортеж.
#     # Из этого кортежа берём элемент с названием function: frame.function.
#     # В этом элементе хранится название вызванной функции.
#     print([frame.function for frame in inspect.stack()])


# def inner():
#     print_call_stack()  # 4, 7


# def outer():
#     print_call_stack()  # 3
#     inner()
#     print_call_stack()  # 5


# # А это ответ на вопрос, который сейчас появится.
# print([frame.function for frame in inspect.stack()])  # 1
# print_call_stack()  # 2
# outer()
# print_call_stack()  # 6
# inner()


# def xggg(applicants, tact, i=None):
#     if len(applicants) == 1:
#         print(applicants[0])
#         return
#     last_gay = tact % len(applicants)
#     if last_gay == 0:
#         del applicants[-1]
#     else:
#         last_values = applicants[last_gay:]
#         del applicants[last_gay - 1:]
#         applicants = last_values + applicants
#     xggg(applicants, tact)


# print(xggg([1, 2, 3, 4, 5], 2))


# def template_sort(len_arr, arr, len_template, template):
#     count = {}
#     for num in arr:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1

#     result = []
#     for num in template:
#         if num in count:
#             result += [num] * count[num]
#             del count[num]
#     for num in sorted(count.keys()):
#         result += [num] * count[num]

#     return ' '.join(map(str, result))


# print(template_sort(10, [2, 4, 3, 5, 5, 6, 0, 9, 8, 7, 7],
#                     6, [2, 4, 3, 5, 6, 0]))


# def block_sort(data_count, arr, count=0, schetchik=1):
#     if len(arr) == 1:
#         count += 1
#         print(count)
#         return
#     if len(arr) == 0:
#         print(count)
#         return
#     min_index = arr.index(min(arr))
#     check_arr = arr[:min_index + schetchik]
#     if len(check_arr) == data_count:
#         print(1)
#         return
#     if max(check_arr) - min(check_arr) == len(check_arr) - 1:
#         len_check_arr = len(check_arr)
#         block_sort(data_count, arr[len_check_arr:], count + 1, schetchik=1)
#     else:
#         check_arr.append(arr[len(check_arr)])
#         block_sort(data_count, arr, count, schetchik=schetchik + 1)


# arr = list(map(int, '3 6 7 4 1 5 0 2'.split()))
# block_sort(8, arr)


# def something(n, min_order_weight, m, sample_weight):
#     left_min = 0
#     left_sample = 0
#     count = 0
#     while n > left_min and m > left_sample:
#         if sample_weight[left_sample] >= min_order_weight[left_min]:
#             count += 1
#             left_min += 1
#         left_sample += 1
#     return count


# min_order_weight = sorted(list(map(int, '8 2 4 7 8 5 5 8 6 9'.split())))
# sample_weight = sorted(list(map(int, '9 8 1 1 1 5 10 8 2 7 4 3 15'.split())))


# print(something(10, min_order_weight, len(sample_weight), sample_weight))


# from pprint import pprint


# def backpack_problem_solution(
#         tools: list[tuple[str, int, int]], capacity: int
# ) -> str:
#     # Сохраняем количество приборов в переменную.
#     items_count = len(tools)
#     # Создаём таблицу. В каждой ячейке должны хранится число и список:
#     # количество экспериментов и список приборов. Для простоты подсчётов 
#     # добавим строку с отсутствием рассматриваемых приборов
#     # и столбец с нулевой вместимостью контейнера.
#     table = [
#         [[0, []] for _ in range(capacity + 1)] for _ in range(items_count + 1)
#     ]
#     # Для каждого прибора:
#     for row_number in range(1, items_count + 1):
#         # Распаковываем кортеж с данными о приборе.
#         name, mass, experiments = tools[row_number - 1]
#         # Для контейнера вместимостью от 1 и до максимальной вместимости:
#         for volume in range(1, capacity + 1):
#             # Если вес прибора меньше или равен 
#             # вместимости рассматриваемого контейнера.
#             if mass <= volume:
#                 # Считаем количество экспериментов для текущего прибора
#                 # плюс наилучшее решение для оставшейся вместимости 
#                 # из предыдущей строки.
#                 total_experiments_with_current_tool = (
#                     experiments + table[row_number - 1][volume - mass][0]
#                 )
#                 # Количество экспериментов 
#                 # в текущей колонке на предыдущей строке:
#                 previous_result = table[row_number - 1][volume][0]
#                 # Если результат с текущим прибором лучше:
#                 if total_experiments_with_current_tool > previous_result:
#                     # Записываем количество экспериментов.
#                     table[row_number][volume][0] = (
#                         total_experiments_with_current_tool
#                     )
#                     # Копируем список приборов из предыдущей строки 
#                     # из ячейки, равной оставшейся вместимости.
#                     table[row_number][volume][1] = list.copy(
#                         table[row_number - 1][volume - mass][1]
#                     )
#                     # Добавляем к списку приборов
#                     # имя текущего прибора.
#                     table[row_number][volume][1].append(name)
#                 else:
#                     # Если результат с рассматриваемым прибором 
#                     # хуже или такой же -
#                     # переносим результат с предыдущей строки.
#                     table[row_number][volume] = table[row_number - 1][volume]
#             else:
#                 # Если масса рассматриваемого прибора 
#                 # больше вместимости ячейки - 
#                 # переносим результат с предыдущей строки.
#                 table[row_number][volume] = table[row_number - 1][volume]
#     # Распечатываем таблицу для проверки.
#     pprint(table)
#     # Возвращаем строку с названиями приборов
#     # из нижней правой ячейки таблицы, через запятую.
#     return ', '.join(table[-1][-1][-1])    


# if __name__ == '__main__':
#     # [('название прибора', масса, количество экспериментов)]
#     tools = [
#         ('гигрометр', 1, 3),
#         ('масс-спектрометр', 4, 6),
#         ('нивелир', 3, 4),
#         ('интерферометр', 1, 4)
#     ]
#     result = backpack_problem_solution(tools, 4)
#     print(result)


def decoding_instructions(instruction):
    stack = []
    current_digit = 0
    result = []

    for i in instruction:
        if i.isdigit():
            current_digit = current_digit * 10 + int(i)
        elif i == '[':
            stack.append((current_digit, result))
            current_digit = 0
            result = []
        elif i == ']':
            prev_num, prev_str = stack.pop()
            result = prev_str + result * prev_num
        else:
            result.append(i)

    return ''.join(result)


print(decoding_instructions('abc2[2[sh]]c3[abc]'))
print(decoding_instructions('10[a]'))
