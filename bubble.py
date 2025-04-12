def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in  range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble([-1, 2, 3, -4]))
                


                
