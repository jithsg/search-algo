def selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(1+i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection([-15, 4, 3, -6]))
    