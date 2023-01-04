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
n= int(input("Enter the number of students who attended the training program: "))

print("\nNow enter the roll nos one by one:")
for i in range(n):
    e=int(input())
    arr.append(e)


key=int(input("\nEnter roll no to search: "))
print("\n1.Binary Search\n2.Fibonacci Search\n")
choice= int(input("Enter choice number for searching: "))
if choice==1:
    
pos=fibo_search(arr,n,key)

print(f"The student is at {pos} position")