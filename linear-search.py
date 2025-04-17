# def linear_search(arr, key):
#     found = False
#     for i in range(len(arr)):
#         if arr[i] == key:
#             print(f"found {key} at {i}  position")
#             found =True
#             break
#     if found == False:
#         print(f"{key} not found")
    
        


# linear_search([1, 5,-7, 8, 0], 95)

def linear_search(arr, key):
    found = False
    list=[]
    for i in range(len(arr)):
        if arr[i] == key:
            # print(f"found {key} at {i}  position")
            found =True
            
            list.append(i)
        
    if found == True:
        print("Key found at")
        for i in list:
            print(i)
    else:
        print("Not found")
    
linear_search([1, 5,-7,-7, 8, 0], -7)