def linear(arr,key):
	for i in arr:
		if i==key:
			#print("student attended training program")
			return 1
	else:
		return 0
		#print("student not attended training program")
	

def linear_recursion(arr,key,i):
	if(i<len(arr)):
		if(arr[i]==key):
			# print("student attended training program")
			return 1
		else:
			linear_recursion(arr,key,i+1)
	else:
		# print("student not attended training program")
		return 0
	
i=0		
arr=[7,9,2,5,3,6]
key=2




flag="y"	
while(flag!="n"):
	print("----------------Menu------------------")
	ch=int(input("Enter your choice:\n1)Linear search\n2)Sentinel search\n\n"))
	match ch:
		case 1:
			res=linear(arr,key)
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")
		case 2:
			res=sentinel(arr,key)
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")


