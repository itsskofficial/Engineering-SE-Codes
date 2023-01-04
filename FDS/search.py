def fibo(n):
    fibo_arr=[0,1]
    for i in range(n):
        ele=fibo_arr[i]+fibo_arr[i+1]
        fibo_arr.append(ele)
    return fibo_arr
    

def fibo_search(arr,n,key):
    fibo_arr=fibo(n)
    f=n
    for i in fibo_arr:
        if i>=n:
            b=fibo_arr[fibo_arr.index(i)-1]
            a=fibo_arr[fibo_arr.index(i)-2]
            break

    while key!=arr[f-1]:
        if key<arr[f-1]:
            f=f-a
            temp1=b
            temp2=a
            b=temp2
            a=temp1-a
        elif key>arr[f-1]:
            f=f+a
            temp1=b
            temp2=a
            b=b-temp2
            a=a-temp1
    return f

arr=[]
n= int(input("Enter the roll nos of students who attended the training program: "))

print("\nNow enter the elements one by one:")
for i in range(n):
    e=int(input())
    arr.append(e)

key=int(input("\nEnter element to search: "))
pos=fibo_search(arr,n,key)

print(f"The element is at {pos} position")