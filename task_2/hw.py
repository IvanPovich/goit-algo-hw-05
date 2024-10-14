def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return (iterations, arr[mid])

    if low < len(arr):
        upper_bound = arr[low]
    return (iterations, upper_bound)

# Приклад використання
arr = [2.1, 3.5, 4.7, 10.3, 40.8]
x = 5.5
result = binary_search(arr, x)

if result[1] is not None:
    print(f"Iterations: {result[0]}, Upper bound: {result[1]}")
else:
    print(f"Iterations: {result[0]}, Upper bound not found")
