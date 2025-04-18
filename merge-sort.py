def merge_sort(arr):
    if len(arr)< 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
    
        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else:
                arr[k] = right[j]
                j+=1
                k+=1
            
        while i< len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j<len(left):
            arr[k] = right[j]
            j+=1
            k+=1
        
        
arr= [-5, -1, 3, 4, 5]
merge_sort(arr)
print(arr)