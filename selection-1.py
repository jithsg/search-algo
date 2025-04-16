

def selection(arr):
    for i in range(0, len(arr)):
        min_index=i
        for j in range(1+i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index =j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



arr = [-8, 0, 8, 1, 9]

print(selection(arr))

    