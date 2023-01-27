arr=[]
n=int(input("Enter no of elements in the array: "))
print("\nEnter the elements one by one now: ")
for i in range(n):
    ele=int(input())
    arr.append(ele)
print(f"You entered the array : {arr}")

def count_sort(arr,n):
    min_ele=min(arr)
    max_ele=max(arr)
    temp1=[]
    temp2=[]
    count=[]
    for i in range(min_ele,max_ele+1):
        temp1.append(i)
    for i in arr:
        c=0
        for j in arr:
            if i==j:
                c+=1
        count.append(c)
    temp2[0]=count[0]
    for i in range(1,len(count)+1):
        temp2[i]=temp2[]
