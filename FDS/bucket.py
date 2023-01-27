arr = []
n = int(input("Enter no of elements in the array: "))
print("\nEnter the elements one by one now: ")
for i in range(n):
    ele = int(input())
    arr.append(ele)
print(f"You entered the array : {arr}")

def bucket_sort(arr,n):
    max_ele=max(arr)
    bucket={}
    if max_ele>100:
        for i in range(0,1001,100):
            bucket[i]=[]
    else:
        for i in range(0,101,10):
            bucket[i]=[]
    keys=bucket.keys()
    for i in arr:
        for j in range(len(keys)):
            temparr=bucket[j]
            if i>keys[j] and i<keys[j+1]:
                temparr.append(i)
            bucket[j]=temparr
    for i in range(len(bucket)):
        temparr=bucket[i]
        for j in range(len(temparr)-1):
            for k in range(0,len(temparr)-j-1):
                if arr[k]>arr[k+1]:
                    temp=temparr[k]
                    temparr[k]=temparr[k+1]
                    temparr[k+1]=temp
        bucket[i]=temparr
    arr=[]
    for i in range(bucket(len)):
        temparr=bucket[i]
        for j in temparr:
            arr.append(j)
    return arr

arr=bucket_sort(arr,n)
print(arr)
