arr = []
n = int(input("Enter no of elements in the array: "))
print("\nEnter the elements one by one now: ")
for i in range(n):
    ele = int(input())
    arr.append(ele)
print(f"You entered the array : {arr}")

def bucket_sort(arr,n):
    max_ele=max(arr)
    high=round()
    bucket={}
    if max_ele>100:
        for i in range(0,1001,100):
            bucket[i]=[]
    else:
        for i in range(0,101,10):
            bucket[i]=[]
    for i in range(len(bucket)):
        temparr=