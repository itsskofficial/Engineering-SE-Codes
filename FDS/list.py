#take user input for three types of players

cricket=input("Enter names of students who play cricket (seperated by commas): ")
cricket_players=cricket.split(',')
badminton=input("\nEnter names of students who play badminton (seperated by commas): ")
badminton_players=badminton.split(',')
football=input("\nEnter names of students who play football (seperated by commas): ")
football_players=football.split(',')

def split(str,char):
  result=[]
  temp=""
  
#print what you got from the user
print (cricket_players)
print (badminton_players)
print (football_players)

#procedure oriented approach used

def crick_bad(cricket,badminton): #students who play both cricket and badminton
  crickbad=[] #define an empty list
  for i in cricket:
    for j in badminton:
      if i==j:
        crickbad.append(i) #if common found append to the empty list
  return crickbad

def crick_or_bad(cricket,badminton,crickbad): #students who play cricket and badminton but not both
  crickorbad=cricket+badminton #concatenate both lists
  for i in crickbad: #check in intersection of set
    for j in crickorbad:
      if i==j:
        crickorbad.remove(i) #if found remove from the list
  return crickorbad

def foot(crickandbad,football): #students who play only football
  onlyfoot=[] #define an empty list
  for i in football:
    onlyfoot.append(i) #append from list to avoid pointer reference
  for i in crickandbad: #check in union of the set
    for j in onlyfoot:
      if i==j:
        onlyfoot.remove(i) #if found then remove from the list
  return onlyfoot

def crick_foot(cricket,badminton,football): #students who play cricket and football but not badminton
  crickfoot=[] #define an empty list
  for i in cricket:
    for j in football:
      if i==j:
        crickfoot.append(i) #append intersection elements
    for i in crickfoot:
      for j in badminton: #check in badminton
        if i==j:
          crickfoot.remove(i) #if common found remove
  return crickfoot

#function calls
crickbad=crick_bad(cricket_players,badminton_players)
crickorbad=crick_or_bad(cricket_players,badminton_players,crickbad)
onlyfoot=foot(cricket_players+badminton_players,football_players) #union of cricket and badminton is passed as first argument
crickfoot=crick_foot(cricket_players,badminton_players,football_players)

#output
print("Students who play both cricket and badminton:")
print(crickbad)
print("Students who play either cricket or badminton but not both:") 
print(crickorbad)
print("Students who play neither cricket nor badminton:" )
print(onlyfoot)
print("Students who play cricket and football but not badminton:")
print(crickfoot)