#take user input for marks
marks=[]
marks_str=input("Enter marks of students roll no wise (enter A for absent): ")
marks_init=marks_str.split(',') #initial marks list
absent=0
for i in marks_init:
	if i!='A':
		marks.append(int(i)) #store if not absent
	else:
		marks.append(i)
		absent+=1 #if absent increment counter
		
#procedure approach is used
def avg(marks,absent):
	sum=0
	average=0
	for i in marks:
		if i!='A': #check if not absent
			sum+=i
	average=sum/(len(marks)-absent) #exclude absent count
	return average


	
def high_low(marks):
	#set first marks encountered to highest and lowest both
	for i in marks:
		if i!='A':
			highest=i
			lowest=i
			break #break to continue from proceeding
	
	#assign highest now
	for i in marks:
		if i!='A' and highest<i:
			highest=i
	high_index=[i+1 for i in range(len(marks)) if marks[i]==highest] #make a list of students roll nos who got the highest marks

	#assign lowest now
	for i in marks:
		if i!='A' and lowest>i:
			lowest=i
	low_index=[i+1 for i in range(len(marks)) if marks[i]==lowest] #make a list of students roll nos who got the lowest marks
	return highest,lowest,high_index,low_index

#check frequency of marks
def frequency(marks):
	n=[]
	for i in marks: #first loop
		m=0
		for j in marks: #second loop for comparing
			if i!='A' and j!='A' and i==j: #if not absent and found then increment frequency by 1
				m+=1
		n.append(m) #append all the frequencies to a list
	return marks[n.index(max(n))] #return the marks which is at the position in n which has highest frequency

#calling functions and displaying output
average=avg(marks,absent)
print(f"\nThe average of marks is: {round(average,2)}")
highest,lowest,high_index,low_index=high_low(marks)
print(f"The highest marks are Roll No: {high_index} Marks: {highest}\nThe lowest marks are Roll No: {low_index} Marks: {lowest}")
print(f"The count of absent students is: {absent}")
freq=frequency(marks)
print(f"The most frequent marks are: {freq}")	
