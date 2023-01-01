def bin_search(arr,l,h,key):
    if (len(arr[l:h])%2!=0):
        low=l
        high=h-1
        mid=int((low+high)/2)
        print(low,high,mid)
    else:
        low=l
        high=h
        mid=int((low+high)/2)
        
    if key==arr[mid]:
        return mid+1
    elif key<arr[mid]:
        return bin_search(arr,0,mid-1,key)
    else:
        return bin_search(arr,mid+1,len(arr),key)

arr=[]
n= int(input("Enter the number of elements: "))

print("\nNow enter the elements one by one:")
for i in range(n):
    e=int(input())
    arr.append(e)

key=int(input("\nEnter element to search: "))
pos=bin_search(arr,0,n,key)

print(f"The element is at {pos} position")