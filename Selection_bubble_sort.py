def selectionSort(array):
	size=len(array)
	for ind in range(size):
		min_index = ind
		for j in range(ind + 1, size):
			if array[j] < array[min_index]:
				min_index = j	
		array[ind], array[min_index] = array[min_index], array[ind]  
	print("sorted list is:")
	print(arr)
        
def bubble_sort(arr):
	for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
		for i in range(n):
			if arr[i] > arr[i + 1]:
				swapped = True
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
	print("sorted list is:")
	print(arr)



size=int(input('Enter number of stundent:'))
arr=[]
for i in range(size):
	x=int(input('Enter roll number:'))
	arr.append(x)

flag='y'
while(flag!="n"):
	ch=int(input('''1) Selection Sort 2) Bubble sort and display top five scores. 3) Exit'''))
	if ch==1:
		print("Unsorted list is:")
		print(arr)
		res=selectionSort(arr)
	if ch==2:
		print("Unsorted list is:")
		print(arr)
		res=bubble_sort(arr)	
	if ch==3:
		flag="n"
	flag=input('Do you want to continue(y/n):')	






