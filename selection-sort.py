
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx =  i
        for j in range(1+i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  
    return arr
    
    
print(selection_sort([-5, -9, 1, 2, 0]))
    
    