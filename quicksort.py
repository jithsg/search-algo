def pivot_place(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True: 
        while left <=right  and list1[left] <= pivot:
            left += 1
    
        while left <= right and list1[right] >= pivot:
            right -= 1
        
        if left > right:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
        
    return right
    
    
def quiksort(list1, first, last):
    if first < last:
        p = pivot_place(list1, first, last)
    
        quiksort(list1, first, p-1)
        quiksort(list1, p+1, last)
    
    
list1= [-3, 5, 6, 7, -1]

n= len(list1)
quiksort(list1, 0, n-1)

print(list1)