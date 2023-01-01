#bubble sort
def bubble(arr,n):
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)

#selection sort
def selection(arr,n):
    min_itself=0
    while min_itself!=n:
        for i in range(n):
            flag = 0
            lowest = arr[i]
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    lowest = arr[j]
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    flag+=1
            if flag==0:
                min_itself+=1
    print(arr)
                
n = int(input("Enter the number of elements in array\n"))
arr =[]

for i in range(n):
    ele = int(input())
    arr.append(ele)
print("Original Array: ")
print(arr)

c = int(input("1.Bubble Sort\n2.Selection Sort\nSelect the method to sort the list: "))
print("Sorted array: ")
if c == 1:
    bubble(arr,n)
elif c == 2:
    selection(arr,n)
else:
    print("Wrong choice")