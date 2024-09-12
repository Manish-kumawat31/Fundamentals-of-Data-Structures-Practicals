# Experiment No. 1 : In a second year computer engineering class, group A students play cricket, group B students play
#                    badminton and group C students play football.
#                    Write a python program using functions to compute following:
#                    a) List of students who play both cricket and badminton.
#                    b) List of students who play either cricket or badminton but not both.
#                    c) Number of students who play neither cricket nor badminton.
#                    d) Number of students who play cricket and football but not badminton.
# (NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)

c=[]
b=[]
f=[]

c1=int(input("enter number of student who play cricket"))
i=1
while(i<=c1):
	roll=int(input("enter Roll numbers:"))
	if roll not in c:
		c.append(roll)
		i+=1
	else:
		pass
b1=int(input("enter number of student who play badminton"))
j=1
while(j<=b1):
	roll=int(input("enter Roll numbers:"))
	if roll not in b:
		b.append(roll)
		j+=1
	else:
		pass
f1=int(input("enter number of student who play football"))
k=1
while(k<=f1):
	roll=int(input("enter Roll numbers:"))
	if roll not in f:
		f.append(roll)
		k+=1
	else:
		pass

u=[]
def union(l1,l2):
	for i in l1:
		u.append(i)
	for j in l2:
		if j not in l1:
			u.append(j)
	return u

inter=[]
def intersection(l1,l2):
	for i in l1:
		if i in l2:
			inter.append(i)
	return inter
	
diff=[]
def differance(l1,l2):
	for i in l1:
		if i not in l2:
			diff.append(i)
	return diff
	

choice='y'
while(choice!='n'):
	print('''Enter choice:
	1) List of students who play both cricket and badminton
	2) List of students who play either cricket or badminton but not both
	3) Number of students who play neither cricket nor badminton
	4) Number of students who play cricket and football but not badminton''')
	ch=int(input())
	match ch:
		case 1:
			u.clear()
			inter.clear()
			diff.clear()
			inter=intersection(c,b)
			print(inter)
		case 2:
			u.clear()
			inter.clear()
			diff.clear()
			union=union(c,b)
			inter=intersection(c,b)
			print(differance(union,inter))
		case 3:
			u.clear()
			inter.clear()
			diff.clear()
			unionRes=union(c,b)
			print(differance(f,unionRes))
		case 4:
			u.clear()
			inter.clear()
			diff.clear()
			inter=intersection(c,f)
			print(differance(inter,b))
	print('Do you want to continue(y/n):')
	choice=input()
		




			
		
