def pivot(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    
    while True:
        while left<= right and arr[left] <= pivot:
            left+=1
    
        while left<= right and arr[right] >= pivot:
            right-=1
        
        if left> right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
        
    return right 
    
    
def qs(arr, first, last):
    if first < last:
        p = pivot(arr, first, last)
        qs(arr, first, p-1)
        qs(arr, p+1, last)
     
list1= [-3, 5, 6, 7, -1]

n= len(list1)
qs(list1, 0, n-1)

print(list1)
        
        
    