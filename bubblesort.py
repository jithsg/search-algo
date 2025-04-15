def bubblesort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubblesort([-1, 2, 3, -4]))

        
        