arr = []
n = int(input("Enter no of elements in the array: "))
print("\nEnter the elements one by one now: ")
for i in range(n):
    ele = int(input())
    arr.append(ele)
print(f"You entered the array : {arr}")


def count_sort(arr,n):
    min_ele = min(arr)
    max_ele = max(arr)
    temp1 = []
    temp2 = []
    count = []
    sorted_arr=[0]*n
    print(sorted_arr)
    for i in range(min_ele, max_ele + 1):
        temp1.append(i)
    print(temp1)
    for i in temp1:
        c = 0
        for j in arr:
            if i == j:
                c += 1
        count.append(c)
    print(count)
    temp2.append(count[0])
    for i in range(1, len(count)):
        temp2.append(temp2[i - 1] + count[i])
    print(temp2)
    for i in arr:
        pos = temp2[(temp1.index(i))]
        print(pos)
        temp2[temp1.index(i)] -= 1
        sorted_arr[pos-1] = i
    return sorted_arr


arr = count_sort(arr,n)
print(arr)
