def binarySearch(arr, x, low, high):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return 0	

def binary_recursion(arr,key,low,high):
	if(low<=high):
		mid=(low+high)//2
		if(arr[mid]==key):
			return 1
		elif(arr[mid]>key):
			high=mid-1
			binary_recursion(arr,key,low,high)
		else:
			low=mid+1
			binary_recursion(arr,key,low,high)
	else:
		return 0
	
def fibMonaccianSearch(arr, key, n):
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected.
    # Note that we compare arr[fibMm2] with x.
    # When fibM becomes 1, fibMm2 becomes 0
    while (fibM > 1):

        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)

        # If x is greater than the value at
        # index fibMm2, cut the subarray array
        # from offset to i
        if (arr[i] < key):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # If x is less than the value at
        # index fibMm2, cut the subarray
        # after i+1
        elif (arr[i] > key):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # element found. return index
        else:
            return 1

    # comparing the last element with x */
    if(fibMMm1 and arr[n-1] == key):
        return 1

    # element not found. return -1
    return 0


arr=[12,24,36,48,60,72,84,96,108,120]
key=12
low=0
high=len(arr)-1
	
	
	
flag="y"	
while(flag!="n"):
	print("----------------Menu------------------")
	ch=int(input("Enter your choice:\n1)binary search\n2)fabonacci search\n3)Exit\n"))
	match ch:
		case 1:
			res=binarySearch(arr,key,low,high)
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")
			flag=input("Do you want to continue(y/n)")
		case 2:
			res=fibMonaccianSearch(arr,key,len(arr))
			if res:
				print("student attended training program\n\n")
			else:
				print("student not attended training program\n\n")
			flag=input("Do you want to continue(y/n)")
		case 3:
			flag="n"
	
