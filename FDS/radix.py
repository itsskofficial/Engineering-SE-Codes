arr=[]
n=int(input("Enter no of elements in the array: "))
print("\nEnter the elements one by one now: ")
for i in range(n):
    ele=int(input())
    arr.append(ele)
print(f"You entered the array : {arr}")

def radix_sort(arr,n):
    radix=[[]]
    max_ele=max(arr)
    highest_place=len(str(max_ele))
    for i in range(highest_place):
        for j in arr:
            rem=j%(10**i)