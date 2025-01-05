# Пошук максимального та мінімального елементів за допомогою методу "розділяй і володарюй"
def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]  # Якщо масив містить один елемент, то він є і мінімумом, і максимумом

    if len(arr) == 2:
        return min(arr[0], arr[1]), max(arr[0], arr[1])  # Якщо два елементи, обчислюємо мінімум і максимум напряму

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max

# Приклад використання
array = [3, 1, 9, 7, 5, 2, 4, 6, 8, 10, 11, 15, 20]
print("Min and Max:", find_min_max(array))