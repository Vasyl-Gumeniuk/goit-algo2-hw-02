my_list = [10, 1, 84, 65, 5, 2, 45, 89, 11, 3, 9]


def find_min_max(arr):
    # Базовий випадок: масив з одного елемента
    if len(arr) == 1:
        return (arr[0], arr[0])

    # Базовий випадок: масив з двох елементів
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    # Знаходимо середину масиву
    mid = len(arr) // 2

    # Рекурсивно знаходимо мін/макс для лівої та правої частин
    left_min, left_max = find_min_max(arr[:mid])  # Ліва половина масиву
    right_min, right_max = find_min_max(arr[mid:])  # Права половина масиву

    # Повертаємо загальний мінімум та максимум
    return (min(left_min, right_min), max(left_max, right_max))



if __name__ == "__main__":
    print(find_min_max(my_list))