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
        for i in range(0,1001)