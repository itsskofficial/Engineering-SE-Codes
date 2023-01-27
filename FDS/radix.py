from copy import deepcopy
arr=[]
n=int(input("Enter no of elements in the array: "))
print("\nEnter the elements one by one now: ")
for i in range(n):
    ele=int(input())
    arr.append(ele)
print(f"You entered the array : {arr}")

def radix_sort(arr,n):
    radix={}
    for i in range(10):
        radix[i]=[]
    print(radix)
    max_ele=max(arr)
    highest_place=len(str(max_ele))
    print(highest_place)
    print(radix)
    for i in range(1,highest_place+1):
        for j in arr:
            if i>1:
                rem=(j%(10**i))//(10**i-1)
            else:
                rem=
            if j not in radix[rem]:
                radix[rem].append(j)
        print(radix)
    arr=[]
    for i in radix:
        for j in i:
            arr.append(j)
radix_sort(arr,n)

