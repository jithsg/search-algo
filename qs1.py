def pivot_point(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left+=1
        while left <= right and arr[right] >= pivot:
            right-=1
        if left>right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right

def qs(arr, first,  last):
    if first< last:
        p= pivot_point(arr, first, last)
        qs(arr, first,  p-1)
        qs(arr, p+1,  last)
        
arr=[-6, 8, 0, 4,-4]
n= len(arr)
qs(arr, 0,  n-1)

print(arr)


    
    
        
        
    
    