def pivot_point(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left+=1
        while left <= right and arr[right] >= pivot:
            right-=1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right

def quicksort(arr, first, last):
    if first<last:
        p= pivot_point(arr, first, last)
        quicksort(arr, first, p-1)
        quicksort(arr, p+1, last)
        
        
arr=[9, -8, -9, 0, 1, 5]

n= len(arr)
quicksort(arr, 0, n-1)   

print(arr)  
     
    
     
     
     


    
    
        

