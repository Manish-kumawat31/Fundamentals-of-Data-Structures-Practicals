def menu():
    L = []
    n = int(input("Enter the number of students = "))
    for i in range(n):
        a = int(input("\nEnter the marks of student(<30,-1 if absent) "+ str(i+1) + ": "))
        while a>30:
            a = int(input("\nInvalid marks\nEnter valid marks(below 30,-1 if absent): "))
        L.append(a)
    f = 0
    while f == 0:
        print("\n----------------------MENU-----------------------")
        print("\n1.Average\n2.Maximum and Minimum\n3.Number of absent students\n4.Highest frequency\n5.Quit")
        ch = int(input("\nChoose your option number = "))
        while ch>5 or ch<1:
            ch = int(input("\nEnter valid option number = "))
        if ch == 1:
            average(L)
        elif ch == 2:
            maxmin(L)
        elif ch == 3:
            absent(L)
        elif ch == 4:
            highf(L)
        elif ch == 5:
            f = 1
            break
        yn = input("\nDo you want to continue(yes or no)? : ")
        if yn == "no":
            break

def average(L):
    sum1 = 0
    count = 0
    for i in L:
        if i != -1:
            sum1 += i
            count += 1
    print("\nAverage result: ",sum1/count)

def maxmin(L):
    max1 = -2
    min1 = 31
    for i in L:
        if i != -1:
            if i > max1:
                max1 = i
            if i < min1:
                min1 = i
    print("\nMaximum = ",max1,"\tMinimum = ",min1)

def absent(L):
    count = 0
    for i in L:
        if i == -1:
            count += 1
    print("\nNumber of absent students = ",count)

def highf(L):
    dict1 = {}
    for i in L:
        if i == -1:
            L.remove(-1)
    for i in range(0,len(L),1):
        if L[i] not in dict1:
            dict1[L[i]] = 1
        else :
            dict1[L[i]] += 1
    freq = list(dict1.values())
    marks = list(dict1.keys())
    max1 = max(freq)
    for i in range(0,len(marks),1):
        if freq[i] == max1:
            print("\nHighest Frequency Marks = ",marks[i],"\tFrequency = ",freq[i])
menu()