def binary_search(arr, key):
    low =0
    high = len(arr) - 1
    
    while low<=high:
        mid = (low + high)//2
    
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid +1
        else:
            high = mid -1
    return -1
        
        

arr = [-10, -3, 0, 2, 4, 7, 9, 12]
key = 19
result = binary_search(arr, key)

print(result)
