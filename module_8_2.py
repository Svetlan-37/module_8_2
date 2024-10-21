def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
            # print(result)
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы : {num}')
    return result, incorrect_data


# print(personal_sum(-15.7, 'tot', 15, 13, [4, 9], 1, {1, 3}))


def calculate_average(numbers):
    try:
        result_2 = personal_sum(numbers)
        return result_2[0] / (len(numbers) - result_2[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average('1, 2, 3')}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Еще Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
