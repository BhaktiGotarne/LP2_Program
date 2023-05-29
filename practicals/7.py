# def selectionSort(arr):
#     for i in range(len(arr)):
#         min = float('-inf')
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i],arr[j] = arr[j], arr[i]
#     return arr
    
# print(selectionSort([89,56,45,34,65,76]))


# def selectionSort(arr):
#     for i in range(len(arr)):
#         min=float('-inf')
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#                 return arr
# print(selectionSort([12,14,87,45,23,90]))



# 

# def selectionSort(arr):
#     for i in range(len(arr)):
#         min=float('-inf')
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#                 return arr
# print(selectionSort([12,14,45,36,87]))            


# def selectionSort(arr):
#     for i in range(len(arr)):
#         min=float('-inf')
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#                 return arr
# print(selectionSort([1,9,0,4,5]))            



def selectionSort(arr):
    for i in range(len(arr)):
        min=float('-inf')
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                return arr
print(selectionSort([23,45,56,78,56,12]))