def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temporary = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temporary
                swapped = True
        if not swapped:
            return arr
