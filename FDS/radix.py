from copy import deepcopy
arr=[]
n=int(input("Enter no of elements in the array: "))
print("\nEnter the elements one by one now: ")
for i in range(n):
    ele=int(input())
    arr.append(ele)
print(f"You entered the array : {arr}")

def radix_sort(arr,n):
    max_ele=max(arr)
    highest_place=len(str(max_ele))
    for i in range(1,highest_place+1):
        radix={}
        for l in range(10):
            radix[l]=[]
        print(radix)
        for j in arr:
            rem=int((j%(10**i))/int((10**(i-1))))
            if j not in radix[rem]:
                radix[rem].append(j)
        print(radix)
        for m in range(0,10):
            temparr=radix[m]
            for j in range(len(temparr)-1):
                for k in range(0,len(temparr)-j-1):
                    if arr[k]>arr[k+1]:
                        temp=temparr[k]
                        temparr[k]=temparr[k+1]
                        temparr[k+1]=temp
            radix[i]=temparr
        arr=[]
        for i in range(10):
            temparr=radix[i]
            for j in temparr:
                arr.append(j)
    
radix_sort(arr,n)

