# Пошук k-го найменшого елемента за допомогою алгоритму Quick Select
def quick_select(arr, k):
    # База рекурсії: якщо масив із одного елемента — це і є шуканий елемент
    if len(arr) == 1:
        return arr[0]

    # Вибираємо опорний елемент
    pivot = arr[len(arr) // 2]

    # Розбиваємо масив на три групи
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Перевіряємо, де знаходиться k-й елемент
    if k <= len(left):
        # Якщо в лівій групі
        return quick_select(left, k)
    elif k <= len(left) + len(mid):
        # Якщо в серединній групі
        return mid[0]
    else:
        # Якщо в правій групі
        return quick_select(right, k - len(left) - len(mid))

# Приклад використання
array = [3, 1, 9, 7, 5, 2, 4, 6, 8, 10, 11, 15, 20]
k = 3
print(f"{k}-й найменший елемент:", quick_select(array, k))