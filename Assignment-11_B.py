def binary(arr,key,low,high):
	while(low<=high):
		mid=(low+high)//2
		if(arr[mid]==key):
			return mid
		elif(arr[mid]>key):
			high=mid-1
		else:
			low=mid+1
	else:
		return 0	

def binary_recursion(arr,key,low,high):
	if(low<=high):
		mid=(low+high)//2
		if(arr[mid]==key):
			return mid
		elif(arr[mid]>key):
			high=mid-1
			binary_recursion(arr,key,low,high)
		else:
			low=mid+1
			binary_recursion(arr,key,low,high)
	else:
		return 0
	

arr=[12,24,36,48,60,72,84,96,108,120]
key=60
low=0
high=len(arr)-1
	
	
	
flag="y"	
while(flag!="n"):
	print("----------------Menu------------------")
	ch=int(input("Enter your choice:\n1)binary search\n2)fabonacci search\n\n"))
	match ch:
		case 1:
			res=binary_recursion(arr,key,low,high)
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")
		case 2:
			res=binary_recursion(arr,key,low,high)
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")
	flag=input("Do you want to continue(y/n)")
