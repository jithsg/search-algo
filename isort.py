def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j=i
    
        while j >0 and key< arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
        arr[j]= key
        
    return arr

print(insertion_sort([5, -1, 4, -3]))