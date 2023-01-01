#accepting inputs
n=int(input("Enter the no of FE students: ")) 
array=[] 
for i in range(n): 
    a=float(input("Enter % of FE students: ")) 
    array.append(a) 


#returning partition element 
def partition(arr, left, right): 
    #rightmost element as pivot
    pivot = arr[right] 
    #pointer 
    i = left - 1
    for j in range(left, right): 
        if arr[j] <= pivot: # j checks if selected element is smaller than pivot
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i]) 
    (arr[i + 1], arr[right]) = (arr[right], arr[i + 1]) 
    # return the position 
    return i + 1


#quick sort function
def quickSort(arr, left, right): 
    if left < right: 
    # finding the pivot element 
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot - 1) 
        quickSort(arr, pivot + 1, right) 
print("The Original Array:", array) 
size = n
quickSort(array, 0, size - 1) 
print('The Sorted Array:', array) 


#displaying top 5 scores
print(" THE TOP FIVE SCORES ARE : ") 
def top(): 
    for i in range(1,6): 
        print(array[-i]) 
top()