my_list = [10, 1, 84, 65, 5, 2, 45, 89, 11, 3, 9]

def quick_select(arr, k):
    # Перевірка коректності вхідних даних
    if k < 1 or k > len(arr):
        raise ValueError("ValueError - k має бути між 1 та довжиною масиву")

    if len(arr) == 1:
        return arr[0]

    # Вибір опорного елемента
    pivot = arr[len(arr) // 2]

    # Розділення масиву на 3 частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):  # k-й елемент знаходиться в лівій частині
        return quick_select(left, k)
    elif k > len(left) + len(middle):  # k-й елемент знаходиться в правій частині
        return quick_select(right, k - len(left) - len(middle))
    else:  # k-й елемент знаходиться в середній частині
        return pivot



if __name__ == "__main__":
    # Знайдемо, наприклад, 6-й найменший елемент
    print(quick_select(my_list, 6))  # Це виведе 6-й найменший елемент у списку
