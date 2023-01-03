matrix1=[]
matrix2=[]
matrix3=[]

rows=int(input("Enter no of rows: "))
cols=int(input("Enter no of columns: "))

#accept two matrices
print("Enter first matrix: ")

for i in range(rows):
	col=[]
	for j in range(cols):
		num=int(input())
		col.append(num)
	matrix1.append(col)

print("Enter second matrix: ")

for i in range(rows):
	col=[]
	for j in range(cols):
		num=int(input())
		col.append(num)
	matrix2.append(col)

#addition
for i in range(rows):
	col=[]
	for j in range(cols):
		sum=matrix1[i][j]+matrix2[i][j]
		col.append(sum)
	matrix3.append(col)

print(f"Addition of two matrices: {matrix3}")

#subtraction
for i in range(rows):
	col=[]
	for j in range(cols):
		res=matrix1[i][j]-matrix2[i][j]
		col.append(res)
	matrix3.append(col)

print(f"Subtraction of two matrices: {matrix3}")

#multiplication 
for i in range(rows):
    col=[]
    for j in range(cols):
        res=0
        for k in range(cols):
            res+=matrix1[i][k]*matrix2[k][j]
        col.append(res)
    matrix3.append(col)

print(f"Multiplication of two matrices: {matrix3}")
for i in matrix3:
	
#transpose
for i in range(cols):
	col=[]
	for j in range(rows):
		num=matrix1[j][i]
		col.append(num)
	matrix3.append(col)

print(f"Transposed matrix of {matrix1} is {matrix3}")