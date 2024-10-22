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

def sentinelSearch(arr, n, key):
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0
    while (arr[i] != key):
        i += 1
    arr[n - 1] = last

    if ((i < n - 1) or (arr[n - 1] == key)):
        return 1
        print(key, "is present at index", i)
    else:
        return 0
        print("Element Not found")


i=0		
arr=[7,9,2,5,3,6]
key=2
n=len(arr)



flag="y"	
while(flag!="n"):
	print("----------------Menu------------------")
	ch=int(input("Enter your choice:\n1)Linear search\n2)Sentinel search\n3)Exit\n"))
	match ch:
		case 1:
			res=linear(arr,key)
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")
		case 2:
			res=sentinelSearch(arr,n,key)
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")
		case 3:
			flag="n"


